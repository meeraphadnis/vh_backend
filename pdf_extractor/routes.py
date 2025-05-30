# routes.py

from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import pdfplumber
import io
from test import find_financial_aid_cost # Assuming this function is defined in test.py
# from extracting_pdf_info import extract_financial_data_from_text

router = APIRouter()


@router.post("/extract-ai")
async def extract_pdf_ai(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    try:
        content = await file.read()
        with pdfplumber.open(io.BytesIO(content)) as pdf:
            full_text = "\n".join(page.extract_text() or "" for page in pdf.pages)
            print(full_text)
        
        with open("extracted_pdf_content.txt", "w", encoding = "utf-8") as file:
            file.write(full_text)

        ai_summary = find_financial_aid_cost("extracted_pdf_content.txt")

        # structured_data = extract_financial_data_from_text(full_text)
        return JSONResponse(content={
            "structured_data": full_text,
            "ai_summary" : ai_summary
              })

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process file: {str(e)}")

# create a route for test
# then test by opening this in our browser with local host (extract API)