# extracting_pdf_info

import os
import openai
from dotenv import load_dotenv

load_dotenv()

def extract_financial_data_from_text(text: str) -> dict:
    """
    Sends raw financial aid text to OpenAI and returns structured financial data.
    """
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

    # Get API key from environment
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment. Please check your .env file.")

    openai.api_key = api_key

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a financial data extractor."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=1000
        )

        # Return the raw response content as a string
        return response.choices[0].message["content"].strip()

    except Exception as e:
        raise Ru
