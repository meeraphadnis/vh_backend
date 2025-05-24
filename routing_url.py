# routing_url.py

from fastapi import APIRouter
from validating_input import FinancialData
from logic import generate_snowball_plan, generate_avalanche_plan
from extracting_pdf_info.routes import router as extracting_pdf_info

router = APIRouter()

@router.post("/repayment-plan")
def repayment(data: FinancialData):
    snowball = generate_snowball_plan(data)
    avalanche = generate_avalanche_plan(data)
    return {
        "snowball": snowball,
        "avalanche": avalanche
    }

router.include_router(extracting_pdf_info, prefix= "/pdf", tags = ["PDF Extraction"])