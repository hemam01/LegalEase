import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


class GeminiDocumentGenerator:

    def __init__(self):
        self.client = None

    def _get_client(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise RuntimeError(
                "GEMINI_API_KEY is not set. Add it to the .env file in the project root."
            )

        if self.client is None:
            self.client = genai.Client(api_key=api_key)

        return self.client

    @staticmethod
    def _extract_text(response):
        if response is None:
            return ""

        if getattr(response, "text", None):
            return response.text

        candidates = getattr(response, "candidates", None) or []
        for candidate in candidates:
            content = getattr(candidate, "content", None)
            parts = getattr(content, "parts", None) or []
            for part in parts:
                text = getattr(part, "text", None)
                if text:
                    return text

        return ""

    @staticmethod
    def _build_fallback_document(document_type: str, parties: str, terms: str, dates: str) -> str:
        return f"""{document_type}

Effective Date: {dates}

This {document_type.lower()} is entered into by and between {parties}.

1. Purpose
The purpose of this {document_type.lower()} is to set out the rights, responsibilities, and obligations of the parties as described in the agreed terms and conditions below.

2. Parties
The parties to this agreement are:
{parties}

3. Terms and Conditions
{terms}

4. Effective Date
This agreement becomes effective on {dates}.

5. Acceptance
By executing or agreeing to this document, the parties acknowledge and accept the obligations set forth herein.

Signed:
________________________
Date: {dates}
"""

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

        try:
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                return self._build_fallback_document(document_type, parties, terms, dates)

            response = self._get_client().models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            document = self._extract_text(response)
            if document and document.strip():
                return document
        except Exception:
            pass

        return self._build_fallback_document(document_type, parties, terms, dates)