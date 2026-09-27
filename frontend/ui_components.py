import streamlit as st


def display_document_preview(document: str):
    st.subheader("Document Preview")

    return st.text_area(
        "Preview / Edit",
        value=document,
        height=500
    )


def display_download_section(txt_data, docx_data, pdf_data):
    st.subheader("Download Document")

    st.download_button(
        "Download TXT",
        data=txt_data,
        file_name="legal_document.txt",
        mime="text/plain"
    )

    st.download_button(
        "Download DOCX",
        data=docx_data,
        file_name="legal_document.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

    st.download_button(
        "Download PDF",
        data=pdf_data,
        file_name="legal_document.pdf",
        mime="application/pdf"
    )
