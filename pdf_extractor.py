# pdf_extractor

from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import pdfplumber
import io
from extracting_pdf_info import extract_financial_data_from_text

router = APIRouter()

@router.post("/extract-ai")
async def extract_pdf_ai(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    try:
        content = await file.read()
        with pdfplumber.open(io.BytesIO(content)) as pdf:
            full_text = "\n".join(page.extract_text() or "" for page in pdf.pages)

        structured_data = extract_financial_data_from_text(full_text)
        return JSONResponse(content={"structured_data": structured_data})

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process file: {str(e)}")
