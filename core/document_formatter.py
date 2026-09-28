from pathlib import Path
from docx import Document
from fpdf import FPDF


def format_txt(content: str) -> str:
    return content


def format_docx(content: str) -> bytes:
    document = Document()

    for line in content.splitlines():
        document.add_paragraph(line)

    output_path = "generated_document.docx"

    document.save(output_path)

    with open(output_path, "rb") as file:
        return file.read()


def format_pdf(content: str) -> bytes:
    pdf = FPDF()

    pdf.add_page()

    # Use a Unicode-compatible font
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed.ttf",
    ]

    font_path = None

    for path in font_paths:
        if Path(path).exists():
            font_path = path
            break

    if font_path:
        pdf.add_font(
            "DejaVu",
            "",
            font_path
        )
        pdf.set_font(
            "DejaVu",
            size=11
        )
    else:
        # Fallback if Unicode font is unavailable
        pdf.set_font(
            "Arial",
            size=11
        )

    pdf.set_auto_page_break(
        auto=True,
        margin=15
    )

    for line in content.splitlines():
        pdf.multi_cell(
            0,
            8,
            line
        )

    output_path = "generated_document.pdf"

    pdf.output(output_path)

    with open(output_path, "rb") as file:
        return file.read()
