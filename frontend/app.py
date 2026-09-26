import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

import os
import streamlit as st
import requests

from core.document_formatter import (
    format_txt,
    format_docx,
    format_pdf
)

from frontend.ui_components import (
    display_document_preview,
    display_download_section
)


st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="wide"
)

BACKEND_URL = os.getenv("LEGAL_EASE_API_URL", "http://127.0.0.1:8000")

st.title("⚖️ LegalEase")
st.subheader("AI-Powered Legal Document Generator")


document_type = st.selectbox(
    "Document Type",
    [
        "Employment Contract",
        "Non-Disclosure Agreement",
        "Lease Agreement",
        "General Contract",
        "Other Agreement"
    ]
)


parties = st.text_area(
    "Parties Involved",
    placeholder="Enter the names/details of the parties..."
)


terms = st.text_area(
    "Terms and Conditions",
    placeholder="Enter the required terms and conditions..."
)


dates = st.text_input(
    "Effective Date",
    placeholder="Enter the effective date..."
)


if st.button("Generate Document"):

    if not parties or not terms or not dates:
        st.warning("Please fill in all required fields.")

    else:
        try:
            response = requests.post(
                f"{BACKEND_URL}/generate",
                json={
                    "document_type": document_type,
                    "parties": parties,
                    "terms": terms,
                    "dates": dates
                }
            )

            if response.status_code == 200:

                result = response.json()

                st.session_state["generated_document"] = result["document"]

                st.success("Document generated successfully!")

            else:
                try:
                    error_detail = response.json().get("detail", response.text)
                except ValueError:
                    error_detail = response.text

                st.error(f"Failed to generate the document. Status code: {response.status_code}")
                st.code(error_detail)

        except requests.exceptions.RequestException:
            st.error(
                "Could not connect to the LegalEase backend. "
                "Please make sure the FastAPI server is running."
            )


if "generated_document" in st.session_state:

    edited_document = display_document_preview(
        st.session_state["generated_document"]
    )

    st.session_state["generated_document"] = edited_document

    txt_data = format_txt(edited_document)
    docx_data = format_docx(edited_document)
    pdf_data = format_pdf(edited_document)

    display_download_section(
        txt_data,
        docx_data,
        pdf_data
    )
