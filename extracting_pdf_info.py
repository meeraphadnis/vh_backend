# extracting_pdf_info.py

import os
import io
import pdfplumber
from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import openai

router = APIRouter()

@router.post("/extract-ai")
async def extract_financial_data_ai(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    try:
        # 1. Read PDF and extract raw text
        content = await file.read()
        with pdfplumber.open(io.BytesIO(content)) as pdf:
            full_text = "\n".join(page.extract_text() or "" for page in pdf.pages)

        # 2. Send to OpenAI for financial data extraction
        openai.api_key = os.getenv("OPENAI_API_KEY")
        prompt = f"""
        Extract the following from this financial aid document and return JSON:
        - Tuition and fees
        - Room and board
        - Transportation
        - Personal expenses
        - Total cost of attendance
        - Loan limits by grade level and type (subsidized/unsubsidized)

        PDF Text:
        {full_text}
        """

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a financial data extractor."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=1000
        )

        extracted_data = response.choices[0].message['content'].strip()
        return JSONResponse(content={"structured_data": extracted_data})

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
