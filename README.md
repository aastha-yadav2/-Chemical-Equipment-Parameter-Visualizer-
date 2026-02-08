# 🚀 Chemical Equipment Parameter Visualizer  
### Hybrid Web + Desktop Application

A complete hybrid application built using **Django REST, React.js, and PyQt5** to analyze and visualize chemical equipment parameters from CSV files.  
The project provides analytics, charts, tables, and PDF reports using a common backend API.

---

## ✨ Key Features

✅ CSV Upload from Web & Desktop  
✅ Data Analytics using Pandas  
✅ Interactive Charts  
- Chart.js (Web)  
- Matplotlib (Desktop)  
✅ Summary Statistics API  
✅ Last 5 Dataset History  
✅ PDF Report Generation  
✅ Clean & User-Friendly UI  

---

## 🧱 Tech Stack

| Layer | Technology |
|-----|------------|
| Backend | Django + Django REST Framework |
| Web Frontend | React.js + Chart.js |
| Desktop Frontend | PyQt5 + Matplotlib |
| Data Processing | Pandas |
| Database | SQLite |

---
## 📂 Project Structure
```bash
chemical-visualizer/
│
├── backend/ # Django API
├── web/ # React Application
├── desktop/ # PyQt Application
├── sample_equipment_data.csv
└── README.md
```
## 📦 Requirements

- Python 3.10+
- Node.js 16+
- Django REST Framework
- PyQt5
- Pandas
- Matplotlib
## 🧩 Architecture

- React & PyQt act as clients  
- Django REST acts as common backend  
- Pandas performs analytics  
- SQLite stores last 5 datasets

---

## ⚙️ Setup & Run

### 1️⃣ Backend

```bash
cd backend
pip install -r requirements.txt
python manage.py runserver
```
## 🔌 API Endpoints

- **/api/upload/** – CSV Upload  
- **/api/summary/** – Analytics & Statistics  
- **/api/pdf/** – Generate PDF Report  

---

## 🌐 Web Application

Run the React frontend:

```bash
cd web
npm install
npm start
```
👉 Open in browser → http://localhost:3000

## 🖥 Desktop Application

Run the PyQt application:

```bash
cd desktop
python app.py
```

---

## 📊 What It Does

### 📥 Input
- Reads chemical equipment CSV file

### 🧠 Calculations
✔ Total equipment  
✔ Average Flowrate  
✔ Average Pressure  
✔ Average Temperature  
✔ Equipment Type Distribution  

### 📈 Displays
🧾 Data Table  
🥧 Pie Chart  
📄 PDF Report  

---

## 🖼 Screenshots

### 🌐 Web Application Dashboard
![Web Application]()

### 🖥 Desktop PyQt Application
![Desktop Application](https://github.com/aastha-yadav2/-Chemical-Equipment-Parameter-Visualizer-/blob/main/Screenshot%202026-02-08%20190241.png)

### 📄 Chart Display
![PDF Report]()

## 🎯 Developed For

**FOSSEE Internship Screening Task**  
💻 Hybrid Web + Desktop Application Challenge  



## 👩‍💻 Author
Aastha Yadav
B.Tech Student | Open Source Enthusiast



