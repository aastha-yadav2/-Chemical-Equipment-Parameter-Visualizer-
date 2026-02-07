from django.urls import path
from .views import UploadCSV, Summary
from .views import UploadCSV, Summary, PDFReport

urlpatterns = [
    path('upload/', UploadCSV.as_view()),
    path('summary/', Summary.as_view()),
    path('pdf/', PDFReport.as_view()),
]
