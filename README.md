# 🚀 Multi-LLM Comparison Tool

A Streamlit-based web application that compares responses from multiple Large Language Models (LLMs) side-by-side.

This tool allows users to evaluate model quality, accuracy, and response time across different AI providers.

---

## 🧠 Integrated Models

- 🔹 OpenAI – GPT-4o-mini
- 🔹 Google Gemini – gemini-2.5-flash
- 🔹 Groq – LLaMA 3.3 70B (versatile)

---

## ✨ Features

- ✅ Side-by-side LLM response comparison
- ⏱️ Response time benchmarking
- 🧩 Modular model integration
- 🔐 Secure API key handling via `.env`
- 🛠️ Clean and scalable project structure
- 🎯 Error handling for each provider

---

## 📂 Project Structure


multi-llm-comparator/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── config/
│ └── settings.py
│
├── llms/
│ ├── openai_model.py
│ ├── gemini_model.py
│ ├── groq_model.py
│
├── utils/
│ └── metrics.py
│
└── .env (not pushed to GitHub)


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/multi-llm-comparator.git
cd multi-llm-comparator
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate     # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
🔑 Environment Variables

Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key
GROQ_API_KEY=your_groq_key

⚠️ Never commit your .env file.

▶️ Run the Application
streamlit run app.py

The app will open in your browser at:

http://localhost:8501
📊 How It Works

User enters a query.

The query is sent to:

OpenAI

Gemini

Groq

Responses are displayed side-by-side.

Response time for each model is measured and shown.

🎯 Use Cases

Model benchmarking

Prompt comparison testing

AI research experiments

Interview demonstration project

Marketing & content strategy evaluation

🏗️ Architecture Overview

Modular LLM abstraction layer

Provider-specific integration modules

Centralized configuration

Reusable performance measurement utility

📈 Future Improvements

Token usage comparison

Cost estimation per query

Response similarity scoring

Hallucination detection layer

Deployment to Streamlit Cloud

👨‍💻 Author

Venkat

📜 License

This project is for educational and demonstration purposes.


---
