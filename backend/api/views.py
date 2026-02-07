from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Dataset
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import FileResponse
import io

class UploadCSV(APIView):

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):

        if 'file' not in request.FILES:
            return Response({"error": "No file provided"}, status=400)

        file = request.FILES['file']

        Dataset.objects.create(file=file)

        # keep only last 5
        if Dataset.objects.count() > 5:
            Dataset.objects.first().delete()

        return Response({"message": "File Uploaded Successfully"})
# ----------- SUMMARY API ------------

class Summary(APIView):

    def get(self, request):

        last = Dataset.objects.last()

        if not last:
            return Response({"error": "No file uploaded yet"})

        df = pd.read_csv(last.file.path)

        data = {
            "total": len(df),
            "avg_flowrate": df["Flowrate"].mean(),
            "avg_pressure": df["Pressure"].mean(),
            "avg_temperature": df["Temperature"].mean(),
            "types": df["Type"].value_counts().to_dict()
        }

        return Response(data)
class PDFReport(APIView):

    def get(self, request):

        last = Dataset.objects.last()
        if not last:
            return Response({"error": "No data"})

        df = pd.read_csv(last.file.path)

        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)

        p.drawString(100, 750, "Chemical Equipment Report")

        y = 700
        p.drawString(50, y, f"Total Equipment: {len(df)}")
        y -= 20
        p.drawString(50, y, f"Avg Flowrate: {df['Flowrate'].mean()}")
        y -= 20
        p.drawString(50, y, f"Avg Pressure: {df['Pressure'].mean()}")
        y -= 20
        p.drawString(50, y, f"Avg Temp: {df['Temperature'].mean()}")

        p.showPage()
        p.save()

        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename="report.pdf")