import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


class GeminiDocumentGenerator:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY is not set in the .env file.")

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel("gemini-1.5-pro")

    def generate_document(
        self,
        document_type: str,
        parties: str,
        terms: str,
        dates: str
    ) -> str:

        prompt = f"""
Generate a structured legal document based on the following information.

Document Type:
{document_type}

Parties:
{parties}

Terms and Conditions:
{terms}

Dates:
{dates}

Requirements:
- Use clear and formal language.
- Organize the document with suitable headings and clauses.
- Include the provided information accurately.
- Do not invent important personal or legal details.
- Return only the document content.
"""

        response = self.model.generate_content(prompt)

        return response.text
