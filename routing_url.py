# routing_url.py

from fastapi import APIRouter, File, UploadFile, HTTPException
from validating_input import FinancialData
from logic import generate_snowball_plan, generate_avalanche_plan
from pdf_extractor.routes import router as pdf_router  # ✅ Include PDF routes
from fastapi.responses import JSONResponse
from test import find_financial_aid_cost

import pdfplumber
import io

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Welcome to the PDF Extraction API. Use /extract-ai to upload a PDF file."}

@router.post("/extract-ai")
async def extract_pdf_ai(file: UploadFile = File(...)):
    print("Received file:")
    
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    try:
        content = await file.read()
        with pdfplumber.open(io.BytesIO(content)) as pdf:
            full_text = "\n".join(page.extract_text() or "" for page in pdf.pages)

        with open("extracted_pdf_content.txt", "w", encoding="utf-8") as f:
            f.write(full_text)

        summary = find_financial_aid_cost("extracted_pdf_content.txt")

        return JSONResponse(content={
            "structured_data": full_text,
            "ai_summary" : summary
            })

    except Exception as e:
        print("Error processing file:", str(e))
        raise HTTPException(status_code=500, detail=f"Failed to process file: {str(e)}")
    
@router.post("/repayment-plan")
def repayment(data: FinancialData):
    snowball = generate_snowball_plan(data)
    avalanche = generate_avalanche_plan(data)
    return {
        "snowball": snowball,
        "avalanche": avalanche
    }

# router.include_router(pdf_router, prefix="/pdf", tags=["PDF Extraction"])
