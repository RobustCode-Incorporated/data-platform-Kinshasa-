import pdfplumber

def read_pdf(pdf_path):
    text_lines = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                text_lines.extend(text.split("\n"))

    return text_lines