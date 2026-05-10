from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file):

    text = ""

    reader = PdfReader(pdf_file)

    for page in reader.pages:
        content = page.extract_text()

        if content:
            text += content

    return text


def split_text(text, chunk_size=1000):

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks