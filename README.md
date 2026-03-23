# 📚 PDF Study Schedule Generator

[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/)  
[![Google Generative AI](https://img.shields.io/badge/Google-GenerativeAI-red?logo=google)](https://cloud.google.com/vertex-ai)

Automatically generates a **one-week study schedule** from any PDF using **Google's Generative AI (Gemini 2.5 Flash)**. Includes summaries, topic breakdowns, and a quiz. The final output is saved as a Markdown file.

---

## ✨ Features

- Extracts text from a PDF (`.pdf`) using `PyPDF2`.
- Generates a study schedule in **Portuguese** (customizable language).
- Provides:
  - 📝 Overview of the content
  - 📖 Topics with summaries
  - ❓ A 5-question quiz with answers
- Saves the result as a Markdown file (`study_schedule.md`).

---

## 🛠️ Requirements

- Python 3.9+
- Packages:
  - `google-generativeai`
  - `PyPDF2`
  - `python-dotenv`

Install dependencies:

pip install google-generativeai PyPDF2 python-dotenv

##⚙️ Setup

Clone the repository.
Create a .env file in the project root with your Google API key:
GOOGLE_API_KEY=your_api_key_here
Place your PDF file in the project directory (e.g., DataBases.pdf).

##🚀 Quick Start

Run the script:

python main.py

The script will:

Extract text from the PDF.
Generate a study schedule using AI.
Save it to study_schedule.md.

##🔧 Customization

Change the language variable to generate the schedule in another language.

##⚠️ Notes

Ensure your Google API key is valid and has access to Generative AI.
AI model used: gemini-2.5-flash.
