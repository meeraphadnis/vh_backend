# extracting_pdf_info

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def extract_financial_data_from_text(text: str) -> str:
    """
    Uses OpenAI SDK v1+ to send text and receive structured financial data as JSON.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing. Please set it in your .env file.")

    # Create OpenAI client
    client = OpenAI(api_key=api_key)

    # Prepare prompt
    prompt = f"""
    Extract and return the following financial information in valid JSON:
    - Tuition and fees
    - Room and board
    - Transportation
    - Personal expenses
    - Total cost of attendance
    - Loan limits by grade level and type (subsidized/unsubsidized)

    PDF Text:
    {text}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a financial data extractor."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=1000
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        raise RuntimeError(f"OpenAI API call failed: {str(e)}")

