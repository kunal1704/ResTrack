import os
import pdfminer
import docx2txt
from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    print("Extracting text from PDF...")
    return extract_text(pdf_path)

def extract_text_from_docx(docx_path):
    print("Extracting text from DOCX...")
    return docx2txt.process(docx_path)

def parse_resume_or_jd(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    
    if file_extension == ".pdf":
        return extract_text_from_pdf(file_path)
    elif file_extension == ".docx":
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format: Only PDF and DOCX are supported")

# Unified function for both resumes and job descriptions
def parse_document(file_path):
    return parse_resume_or_jd(file_path)

# Example usage
# resume_text = parse_document("data/resumes/sample_resume.pdf")
# jd_text = parse_document("data/job_descriptions/sample_jd.pdf")
