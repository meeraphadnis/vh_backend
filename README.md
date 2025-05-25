# vh_backend

📘 Loan Repayment Planner – Backend

This is the backend service for a Loan Repayment Planner app. Using the API of Google's LLM Gemini, it can take in PDFs of the student's financial aid statement and extract the necessary numerical values (total loan principal, total unmet need, etc.) to calculate the student's best suited loan repayment strategy.

🚀 Features

  📊 Calculates Snowball and Avalanche repayment plans

  🧠 Supports financial data input via JSON

  📟 Upload PDFs for AI-based document parsing (using Gemini, Google's LLM, API)

  🔀 Integrated with frontend

💪 Tech Stack

  FastAPI – Web framework

  Uvicorn – ASGI server

  pdfplumber – PDF text extraction

  python-dotenv – Manage environment variables

  python-multipart – Handle file uploads

  google-generativeai – LLM-based text extraction

  pdf2image – (Optional) Convert PDFs to images for advanced processing

📂 File Structure

VH_BACKEND/
│
├── .env # API keys and environment config
├── main.py # FastAPI app entry point
├── routing_url.py # All routes including /repayment-plan, /pdf/extract
├── logic.py # Core repayment plan logic (snowball & avalanche)
├── validating_input.py # Pydantic models for validation
├── extracting_pdf_info.py # Calls OpenAI/Gemini to extract structured data from PDFs
├── pdf_extractor.py # Alternate PDF extraction logic
├── convert_pdf_png.py # Optional: Convert PDF to image
├── gemini_api_key # (Temporary) key store
├── extracted_pdf_content.txt# Sample output for debugging
├── test.py # Testing endpoint or experiments
│
├── pdf_extractor/ # PDF-related FastAPI routes
│
├── sample-aid.pdf # Test PDFs
├── sample.pdf
├── page_converted.png # Image conversion test
│
├── requirements.txt # Python dependencies
├── package.json # Node-related test scripts (if any)
└── README.md

📦 Installation

git clone https://github.com/yourusername/loan-repayment-backend.git
cd loan-repayment-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

▶️ Run the Server

uvicorn main:app --reload

Open in browser:👉 http://127.0.0.1:8000

🔌 API Endpoints

POST /repayment-plan

Submit loan + income data and get snowball and avalanche schedules.

GET /history

Retrieve all previously calculated repayment plans.

DELETE /history (optional)

Clear saved repayment history.

POST /pdf/extract-ai (optional)

Upload a financial aid PDF and extract key values (requires OpenAI API key).

🧠 Future Improvements

Backend is not returning to allow frontend to take its values; frontend dashboard integration

Login system to store user inputs

🏁 Authors & Credits

  Arena Galeana

  Ahona Khandaker

  Sanaa Bebal

  Meera Phadnis

Built with ❤️ for Venus Hacks on May 2025

