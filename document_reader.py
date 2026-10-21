import os
from pypdf import PdfReader

def extract_text_from_pdf(uploaded_file):
    """
    Accepts a Streamlit uploaded file object, reads it using pypdf,
    and returns the extracted text combined from all pages.
    """
    try:
        # Create a PDF reader object using the uploaded file stream
        reader = PdfReader(uploaded_file)
        
        # Check if the PDF has pages
        if len(reader.pages) == 0:
            return None, "The uploaded PDF file is empty."
        
        extracted_text = ""
        # Loop through each page and extract text
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                extracted_text += text + f"\n[Page {i+1}]\n"
                
        # Check if text extraction yielded anything meaningful
        if not extracted_text.strip():
            return None, "No readable text found. This might be a scanned image-only PDF."
            
        return extracted_text, None
        
    except Exception as e:
        return None, f"Error reading PDF file: {str(e)}"