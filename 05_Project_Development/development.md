# Phase 5: Project Development

## Project Title

LegalEase – AI-Powered Legal Document Generator

## 1. Development Overview

The development phase involves implementing the LegalEase application using Python, Streamlit, FastAPI, Google Gemini, and document-generation libraries.

The application is developed using a modular structure so that the frontend, backend, AI functionality, and document formatting components can be maintained separately.

## 2. Development Environment

The project was developed using:

- Python
- Visual Studio Code
- Git
- GitHub
- Virtual environment
- Web browser

## 3. Project Structure

The main application components are organized as follows:

```text
LegalEase/
│
├── ai_core/
│   └── gemini_generator.py
│
├── backend/
│   ├── main.py
│   └── routes.py
│
├── core/
│   └── document_formatter.py
│
├── frontend/
│   ├── app.py
│   └── ui_components.py
│
├── tests/
│   └── test_gemini_generator.py
│
├── Architecture/
├── deployment/
├── docs/
└── setup/
