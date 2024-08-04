"""console_app.py"""

from docx import Document

def create_docx(text: str) -> None:
    doc = Document()
    doc.add_paragraph(text)
    doc.save('user_text.docx')

if __name__ == "__main__":
    text = input("Enter a text: ")
    create_docx(text)
