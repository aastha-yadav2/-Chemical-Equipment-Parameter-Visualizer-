import sys
import requests
import pandas as pd
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


API_BASE = "http://127.0.0.1:8000/api"


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chemical Equipment Visualizer")
        self.setGeometry(200, 200, 800, 600)

        layout = QVBoxLayout()

        # ---- Upload ----
        self.uploadBtn = QPushButton("Upload CSV")
        self.uploadBtn.clicked.connect(self.upload_csv)
        layout.addWidget(self.uploadBtn)

        # ---- Summary Label ----
        self.label = QLabel("No Data")
        layout.addWidget(self.label)

        # ---- Table ----
        self.table = QTableWidget()
        layout.addWidget(self.table)

        # ---- Chart ----
        self.chartBtn = QPushButton("Show Chart")
        self.chartBtn.clicked.connect(self.show_chart)
        layout.addWidget(self.chartBtn)

        self.setLayout(layout)

        self.load_summary()


    def upload_csv(self):

        path, _ = QFileDialog.getOpenFileName(
            self, "Select CSV", "", "CSV Files (*.csv)"
        )

        if not path:
            return

        files = {'file': open(path, 'rb')}

        res = requests.post(API_BASE + "/upload/", files=files)

        if res.status_code == 200:
            QMessageBox.information(self, "Success", "Uploaded Successfully")
            self.load_summary()
        else:
            QMessageBox.warning(self, "Error", str(res.json()))


    def load_summary(self):

        res = requests.get(API_BASE + "/summary/")

        if res.status_code != 200:
            return

        data = res.json()

        text = f"""
Total: {data['total']}
Avg Flowrate: {data['avg_flowrate']}
Avg Pressure: {data['avg_pressure']}
Avg Temp: {data['avg_temperature']}
        """

        self.label.setText(text)

        self.types = data["types"]

        # ---- Fill Table ----
        self.table.setRowCount(len(self.types))
        self.table.setColumnCount(2)

        self.table.setHorizontalHeaderLabels(["Type", "Count"])

        for i, (k, v) in enumerate(self.types.items()):
            self.table.setItem(i, 0, QTableWidgetItem(str(k)))
            self.table.setItem(i, 1, QTableWidgetItem(str(v)))


    def show_chart(self):

        if not hasattr(self, 'types'):
            return

        labels = list(self.types.keys())
        values = list(self.types.values())

        plt.figure(figsize=(5,5))
        plt.pie(values, labels=labels, autopct='%1.1f%%')
        plt.title("Equipment Type Distribution")
        plt.show()



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
