# ⚖️ LegalEase
### AI-Powered Legal Document Generator

## 📌 Project Overview

LegalEase is an AI-powered web application that helps users generate structured legal documents using Generative AI.

Users can enter basic information such as document type, parties, terms and conditions, and dates. The system uses Google Gemini to generate the document and allows users to preview, edit, and download it.

> ⚠️ LegalEase is an AI-assisted document generation tool and is not a substitute for professional legal advice.

---

## 🎯 Problem Statement

Creating legal documents manually can be time-consuming and difficult for users who are unfamiliar with legal terminology and document formats.

Users may find it difficult to properly organize:

- Parties involved
- Terms and conditions
- Dates
- Legal clauses
- Document formatting

---

## 💡 Proposed Solution

LegalEase simplifies document creation using Generative AI.

The application:

1. Accepts document details from the user.
2. Sends the information to the FastAPI backend.
3. Uses Google Gemini to generate the document.
4. Displays the generated document.
5. Allows users to preview and edit it.
6. Provides TXT, DOCX, and PDF download options.

---

## ✨ Key Features

- ⚖️ AI-powered legal document generation
- 📝 Simple user interface
- 🤖 Google Gemini integration
- 👀 Document preview
- ✏️ Document editing
- 📄 TXT export
- 📑 DOCX export
- 📕 PDF export
- ⚡ FastAPI backend
- 🖥️ Streamlit frontend
- 🌐 Web deployment

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Frontend |
| FastAPI | Backend API |
| Google Gemini | Generative AI |
| Pydantic | Data validation |
| Python-docx | DOCX generation |
| FPDF | PDF generation |
| Requests | API communication |
| Git & GitHub | Version control |

---

## 🏗️ System Architecture

```text
             👤 User
                │
                ▼
      🖥️ Streamlit Frontend
                │
                ▼
       ⚡ FastAPI Backend
                │
                ▼
          🤖 Google Gemini
                │
                ▼
       📄 Generated Document
                │
                ▼
          👀 Preview / Edit
                │
        ┌───────┼───────┐
        ▼       ▼       ▼
       TXT     DOCX     PDF
