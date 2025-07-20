# resumechecker
import fitz  # PyMuPDF
from docx import Document
from io import BytesIO

def extract_text_from_pdf(data: bytes) -> str:
    with fitz.open(stream=data, filetype="pdf") as doc:
        return "\n".join(page.get_text() for page in doc)

def extract_text_from_docx(data: bytes) -> str:
    doc = Document(BytesIO(data))
    return "\n".join(p.text for p in doc.paragraphs)

def analyze_resume(data: bytes, filename: str) -> dict:
    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(data)
    elif filename.endswith(".docx"):
        text = extract_text_from_docx(data)
    else:
        return {"error": "Unsupported file format."}

    sections = {
        "Education": "education",
        "Experience": "experience",
        "Skills": "skills",
        "Projects": "project",
        "Certifications": "certification"
    }

    score = 0
    suggestions = []

    for label, keyword in sections.items():
        if keyword.lower() in text.lower():
            score += 20
        else:
            suggestions.append(f"Add a {label} section.")

    return {
        "score": score,
        "summary": f"Your resume scored {score}/100",
        "suggestions": suggestions
    }
