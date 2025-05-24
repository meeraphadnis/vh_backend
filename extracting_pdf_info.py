from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import pdfplumber
import io

app = FastAPI()

@app.post("/extract")
async def extract_pdf_data(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    result = {"text": "", "numbers": []}

    try:
        file_content = await file.read()
        with pdfplumber.open(io.BytesIO(file_content)) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    result["text"] += text + "\n"
                    # Extract numbers
                    numbers = [
                        float(word.replace(",", ""))
                        for word in text.split()
                        if word.replace(",", "").replace(".", "", 1).isdigit()
                    ]
                    result["numbers"].extend(numbers)

        return JSONResponse(content=result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")
