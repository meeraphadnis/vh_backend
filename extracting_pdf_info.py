# extracting_pdf_info.py

import os
import openai
from dotenv import load_dotenv

load_dotenv()

def extract_financial_data_from_text(text: str) -> dict:
    prompt = f"""
    Extract the following from this financial aid document and return JSON:
    - Tuition and fees
    - Room and board
    - Transportation
    - Personal expenses
    - Total cost of attendance
    - Loan limits by grade level and type (subsidized/unsubsidized)

    PDF Text:
    {text}
    """

    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a financial data extractor."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=1000
    )

    return response.choices[0].message["content"].strip()
