# LegalEase - Project Workflow

## 1. User Input

The user provides the required information through the Streamlit frontend.

The inputs include:
- Document type
- Parties involved
- Terms and conditions
- Effective date

## 2. Streamlit Frontend

The Streamlit interface collects the user's inputs and sends them to the FastAPI backend.

## 3. FastAPI Backend

The FastAPI backend receives the request through the `/generate` endpoint and validates the input.

## 4. Gemini AI Integration

The backend sends the required information to the Gemini Generative AI model through the AI integration module.

## 5. Legal Document Generation

Gemini generates structured legal content based on the user's inputs.

## 6. Preview and Editing

The generated document is displayed in the Streamlit interface. The user can preview and edit the generated content.

## 7. Document Formatting and Export

The generated content can be formatted and downloaded in:
- TXT
- DOCX
- PDF

## 8. Testing and Deployment

The complete application is tested locally to verify that the frontend, backend, AI integration, and document exports work correctly.
