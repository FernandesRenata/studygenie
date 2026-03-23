import google.generativeai as genai
from PyPDF2 import PdfReader as PDF
import os
from dotenv import load_dotenv

#extract content from the document
reader = PDF("DataBases.pdf")
full_text = ""

for page in reader.pages:
    full_text += page.extract_text()

#configure the AI settings

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("The API key was not found! Please check the .env file.")
else:
    print(f"API key loaded successfully!")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('models/gemini-2.5-flash')
language = "Portuguese"

#generate the schedule
def generate_study_schedule(full_text, language):
    prompt = f"""
    
    1. Write a one-week study schedule.
    2. Provide an overview of the content in a maximum of five lines.
    3. List the topics with a summary of each one.
    4. Create a quiz with five questions and their answers.
    5. Use the {language} language.
    Content: {full_text[:15000]}
    """
    
    response = model.generate_content(prompt)
    return response.text

result = generate_study_schedule(full_text, language)

def save_to_markdown(content, filename="study_schedule.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"The file: {filename} was saved!")

save_to_markdown(result)