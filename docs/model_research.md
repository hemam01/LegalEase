# LegalEase - Generative AI Model Research

## 1. Project Requirement

LegalEase requires a Generative AI model to create structured legal documents based on user-provided information.

The required inputs include:

- Document type
- Parties involved
- Terms and conditions
- Effective date

## 2. Model Research

The project uses Google's Gemini Generative AI model for legal document generation.

The model is evaluated based on its ability to:

- Understand long and structured inputs
- Generate formal and organized content
- Follow structured prompts
- Generate clauses based on user requirements
- Produce suitable content for different types of legal documents

## 3. Selected Model

The selected model for the project is:

**Gemini 1.5 Pro**

## 4. Reason for Selection

Gemini 1.5 Pro is selected because it is suitable for generating structured documents from user-provided information.

The project documentation identifies the following capabilities:

- Long context window
- Structured prompting with multi-part content
- Fast generation
- Ability to generate formal documents
- Ability to dynamically generate clauses based on user inputs

## 5. Legal Document Types

The AI system can be used to generate documents such as:

- Employment Contracts
- Non-Disclosure Agreements (NDA)
- Lease Agreements
- Contracts
- Other agreements

## 6. AI Integration

The Gemini model will be integrated into the LegalEase application through the AI core.

The integration will use:

`ai_core/gemini_generator.py`

This module will receive the required information, create a structured prompt, send it to Gemini, and return the generated legal content.

## 7. Expected Output

The selected AI model should generate structured legal content that can then be:

- Previewed
- Edited
- Formatted
- Downloaded as TXT
- Downloaded as DOCX
- Downloaded as PDF
