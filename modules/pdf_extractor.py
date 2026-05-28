import io
import re
from PyPDF2 import PdfReader

def extract_text_from_pdf(uploaded_file) -> dict:
    """
    Ingests an uploaded file buffer, parses text metrics page-by-page,
    and returns sanitized strings alongside structural state responses.
    """
    response = {
        "text": "",
        "pages": 0,
        "success": False,
        "error": None
    }
    
    try:
        pdf_data = uploaded_file.read()
        pdf_file = io.BytesIO(pdf_data)
        reader = PdfReader(pdf_file)
        
        total_pages = len(reader.pages)
        response["pages"] = total_pages
        
        if total_pages == 0:
            response["error"] = "The uploaded PDF contains no structural pages."
            return response
            
        full_text_list = []
        for page_num in range(total_pages):
            page_text = reader.pages[page_num].extract_text()
            if page_text:
                full_text_list.append(page_text)
                
        raw_text = "\n".join(full_text_list)
        
        # Clean multi-line whitespace fragments safely
        cleaned_text = re.sub(r'[ \t]+', ' ', raw_text)
        cleaned_text = re.sub(r'\n\s*\n', '\n', cleaned_text)
        
        if not cleaned_text.strip():
            response["error"] = "Failed to extract clean text characters (Document might be image-only scan)."
            return response
            
        response["text"] = cleaned_text.strip()
        response["success"] = True
        
    except Exception as e:
        response["error"] = f"Extraction internal structural error: {str(e)}"
        
    return response