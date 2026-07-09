# 🤖 QueryMind AI

> AI-Powered SQL Analytics Platform built with Streamlit, SQLite, and Google Gemini.

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 📌 Overview

QueryMind AI is an intelligent SQL analytics platform that allows users to analyze datasets using natural language.

Simply upload your data, ask questions in plain English, and QueryMind AI generates SQL queries, executes them, visualizes results, and provides AI-powered business insights.

---

## 🚀 Live Demo

🔗 **Streamlit App:**  
https://querymind-ai-o5szprn2tmcm56emxxfjtv.streamlit.app/


## ✨ Features

- 🤖 AI SQL Generation
- 📊 Interactive Dashboard
- 📈 Automatic Data Visualization
- 💡 AI Business Insights
- 📄 PDF Report Generation
- 📥 CSV Download
- 📚 Query History
- 🛡 SQL Safety Validation
- ⚡ Fast SQLite Execution
- 🎨 Premium Dark UI

---

## 🛠 Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### AI

- Google Gemini API

### Database

- SQLite

### Data Processing

- Pandas
- NumPy

### Visualization

- Plotly

### Reports

- ReportLab

---

## 📂 Project Structure

```
QueryMind-AI
│
├── assets/
├── database/
├── pages/
├── services/
├── utils/
├── Home.py
├── requirements.txt
└── README.md
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/Divyansh022006/QueryMind-AI.git
```

Move into project

```bash
cd QueryMind-AI
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create

```
.streamlit/secrets.toml
```

Add

```toml
GEMINI_API_KEY="YOUR_API_KEY"
```

---

## ▶ Run

```bash
streamlit run Home.py
```

---

## 💬 Example Questions

```
Show all data

Top 10 rows

Count all records

Highest selling product

Average sales

Revenue by category

Top 5 customers

Which region generated the highest sales?

Monthly revenue

Average quantity sold
```

---

## 📊 Workflow

```
Upload Dataset
        │
        ▼
Read Schema
        │
        ▼
Natural Language Question
        │
        ▼
Gemini AI
        │
        ▼
Generate SQL
        │
        ▼
SQL Validation
        │
        ▼
SQLite Execution
        │
        ▼
Visualization
        │
        ▼
Business Insights
        │
        ▼
PDF Report
```

---

## 🎯 Future Improvements

- Multi-table SQL Support
- Authentication
- Chat History
- Dashboard Sharing
- PostgreSQL Support
- MySQL Support
- CSV Upload from URL
- LLM Agent Workflow
- Voice Queries
- AI Dashboard Builder

---

## 👨‍💻 Author

### Divyansh Agarwal

GitHub

https://github.com/Divyansh022006

LinkedIn

_Add your LinkedIn link_

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---

## 📜 License

This project is licensed under the MIT License.
