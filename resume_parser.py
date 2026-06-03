from PyPDF2 import PdfReader
from docx import Document

def file_extraction(file):
    if file.name.endswith(".pdf"):
        reader=PdfReader(file)
        text=""

        for page in reader.pages:
            text +=page.extract_text()

        return text
    
    elif file.name.endswith(".docx"):
        doc=Document(file)

        text="" 

        for para in doc.paragraphs:
            text+=para.text +"\n"

        return text

    else:
        return "Unsupported file format"


    