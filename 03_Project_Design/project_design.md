**# Phase 3: Project Design

## Project Title

LegalEase – AI-Powered Legal Document Generator

## 1. System Architecture

LegalEase follows a modular architecture consisting of:

- Streamlit frontend
- FastAPI backend
- Google Gemini Generative AI
- Document formatting module
- TXT, DOCX, and PDF export

## 2. System Workflow

The system works through the following steps:

1. User opens the LegalEase application.
2. User enters the required document details.
3. Streamlit frontend collects the information.
4. The frontend sends the request to the FastAPI backend.
5. FastAPI processes the request.
6. The backend sends the information to Google Gemini.
7. Gemini generates the legal document content.
8. The generated content is returned to the frontend.
9. The user can preview and edit the document.
10. The user can download the document as TXT, DOCX, or PDF.

## 3. Main Components

### Frontend

Technology: Streamlit

Responsibilities:

- Collect user input
- Send requests to the backend
- Display generated documents
- Provide document preview and editing
- Provide download options

### Backend

Technology: FastAPI

Responsibilities:

- Receive frontend requests
- Validate input data
- Communicate with the AI model
- Return generated document content

### AI Module

Technology: Google Gemini

Responsibilities:

- Process the user's document information
- Generate structured legal document content
- Organize the content using suitable headings and clauses

### Document Formatter

Responsibilities:

- Convert generated content into TXT format
- Generate DOCX files
- Generate PDF files

## 4. Data Flow

```text
User
  ↓
Streamlit Frontend
  ↓
FastAPI Backend
  ↓
Gemini AI
  ↓
Generated Legal Document
  ↓
Frontend Preview/Edit
  ↓
TXT / DOCX / PDF**
