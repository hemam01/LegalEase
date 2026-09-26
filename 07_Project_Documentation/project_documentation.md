# Phase 7: Project Documentation

## Project Title

LegalEase – AI-Powered Legal Document Generator

## 1. Project Overview

LegalEase is an AI-powered application designed to help users generate structured legal documents from basic information provided by them.

The application uses Generative AI to create document content and provides a simple interface for previewing, editing, and downloading the generated document.

The project combines a Streamlit frontend, FastAPI backend, Google Gemini AI, and document formatting libraries.

---

## 2. Problem Statement

Creating legal documents manually can be time-consuming and difficult for users who are not familiar with legal document formats and terminology.

Users may find it difficult to organize information such as parties, terms, conditions, and dates into a properly structured document.

LegalEase aims to simplify this process by using Generative AI to assist with document generation.

---

## 3. Proposed Solution

LegalEase allows users to enter basic information about the document they want to create.

The application sends the information to the backend, which communicates with Google Gemini to generate structured document content.

The generated document can then be previewed, edited, and downloaded in different formats.

---

## 4. Objectives

The main objectives of the project are:

- To develop an AI-powered legal document generation system.
- To simplify the process of creating structured documents.
- To integrate Generative AI into a practical application.
- To provide a simple and user-friendly interface.
- To allow users to preview and edit generated content.
- To support TXT, DOCX, and PDF downloads.
- To demonstrate frontend, backend, AI integration, and deployment.

---

## 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Frontend user interface |
| FastAPI | Backend API |
| Google Gemini | Generative AI |
| Python-docx | DOCX generation |
| FPDF | PDF generation |
| Requests | Frontend-backend communication |
| Pydantic | Data validation |
| Uvicorn | Backend server |
| GitHub | Version control and collaboration |
| Render | Backend deployment |
| Streamlit Community Cloud | Frontend deployment |

---

## 6. System Architecture

The application consists of the following major components:

### Frontend

The Streamlit frontend collects information from the user and displays the generated document.

### Backend

The FastAPI backend receives requests from the frontend and manages communication with the AI module.

### AI Module

Google Gemini is used to generate structured legal document content based on the information provided by the user.

### Document Formatter

The document formatter converts the generated content into TXT, DOCX, and PDF formats.

---

## 7. System Workflow

The overall workflow is:

```text
User
  ↓
Streamlit Frontend
  ↓
FastAPI Backend
  ↓
Google Gemini AI
  ↓
Generated Legal Document
  ↓
Preview / Edit
  ↓
TXT / DOCX / PDF
