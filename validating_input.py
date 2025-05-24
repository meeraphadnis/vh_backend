from pydantic import BaseModel
from typing import List

class LoanInput(BaseModel):
    name: str
    balance: float
    interest_rate: float
    min_payment: float

class FinancialData(BaseModel):
    loans: List[LoanInput]
    monthly_income: float
    monthly_expenses: float
