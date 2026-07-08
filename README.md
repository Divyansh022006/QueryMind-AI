# 🧠 QueryMind AI

<p align="center">

</p>

<p align="center">

AI-Powered SQL Analytics Platform built with **Streamlit**, **Ollama**, **Qwen2.5**, **SQLite**, and **Plotly**.

Convert natural language into SQL queries, analyze datasets, visualize results, and generate AI-powered business insights — all from a simple web interface.

</p>

---

## ✨ Features

- 📁 Upload CSV datasets
- 🗄️ Automatic SQLite database creation
- 🤖 Natural Language → SQL using AI
- 💻 Manual SQL Query Runner
- 📊 Interactive Analytics Dashboard
- 📈 Automatic Data Visualization
- 💡 AI Business Insights
- 📑 Dataset Profiling
- 📜 Query History
- 📄 PDF Report Generation
- 🎨 Modern Dark UI
- 📥 Export Results as CSV

---


# 🏗 Project Architecture

```
                CSV Dataset
                     │
                     ▼
           Upload Dataset Page
                     │
                     ▼
              SQLite Database
                     │
        ┌────────────┴────────────┐
        │                         │
        ▼                         ▼
 AI SQL Generator           SQL Query Runner
        │                         │
        └────────────┬────────────┘
                     ▼
             Execute SQL Query
                     │
         ┌───────────┼────────────┐
         ▼           ▼            ▼
     Data Table   Visualizations  AI Insights
                     │
                     ▼
               PDF Report Export
```

---

# 🚀 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Frontend | Streamlit |
| Database | SQLite |
| AI Model | Ollama + Qwen2.5 |
| Data Analysis | Pandas |
| Visualization | Plotly |
| Reports | ReportLab |
| Styling | Custom CSS |

---

# 📂 Project Structure

```
QueryMind-AI
│
├── assets/
│   ├── banner.png
│   ├── logo.png
│   └── style.css
│
├── database/
│
├── pages/
│
├── services/
│
├── utils/
│
├── requirements.txt
│
├── 🏠_Home.py
│
└── README.md
```

---

# ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/Divyansh022006/QueryMind-AI.git

cd QueryMind-AI
```

---

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Mac/Linux

```bash
source .venv/bin/activate
```

---

### Install Requirements

```bash
pip install -r requirements.txt
```

---

### Install Ollama

Download from

https://ollama.com

Pull the model

```bash
ollama pull qwen2.5:3b
```

Start Ollama

```bash
ollama serve
```

---

### Run the App

```bash
streamlit run 🏠_Home.py
```

---

# 💡 Example Questions

- Show all records
- Count all orders
- Show revenue by category
- Highest selling product
- Top 5 customers
- Average quantity sold
- Which region has the highest sales?
- Show monthly revenue

---

# 🌟 Future Enhancements

- AI Data Cleaning
- Predictive Analytics
- AutoML Integration
- Chat Memory
- Dashboard Builder
- User Authentication
- Cloud Deployment
- Multi-Agent AI Support

---

# 📊 Skills Demonstrated

- Python
- SQL
- SQLite
- Streamlit
- Pandas
- Plotly
- AI Integration
- Ollama
- Prompt Engineering
- Data Visualization
- Business Analytics
- Software Engineering

---

# ⚠️ Note

This project uses **Ollama** with the **Qwen2.5** language model for local AI inference.

Because Ollama runs locally, AI-powered features require Ollama to be installed and running on your machine.

---

# 👨‍💻 Developer

**Divyansh Agarwal**

GitHub

https://github.com/Divyansh022006

---

## ⭐ If you found this project useful, please consider giving it a star!
