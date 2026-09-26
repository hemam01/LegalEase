import streamlit as st
import requests

from core.document_formatter import (
    format_docx,
    format_pdf,
    format_txt
)


st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="wide"
)

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
                "http://127.0.0.1:8000/generate",
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
                st.error("Failed to generate the document.")

        except requests.exceptions.RequestException:
            st.error(
                "Could not connect to the LegalEase backend. "
                "Please make sure the FastAPI server is running."
            )


if "generated_document" in st.session_state:

    st.subheader("Generated Document")

    edited_document = st.text_area(
        "Preview / Edit",
        value=st.session_state["generated_document"],
        height=500
    )

    st.session_state["generated_document"] = edited_document

    txt_data = format_txt(edited_document)
    docx_data = format_docx(edited_document)
    pdf_data = format_pdf(edited_document)

    st.subheader("Download Document")

    st.download_button(
        label="Download TXT",
        data=txt_data,
        file_name="legal_document.txt",
        mime="text/plain"
    )

    st.download_button(
        label="Download DOCX",
        data=docx_data,
        file_name="legal_document.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

    st.download_button(
        label="Download PDF",
        data=pdf_data,
        file_name="legal_document.pdf",
        mime="application/pdf"
    )
    
