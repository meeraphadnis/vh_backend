# logic.py

from validating_input import FinancialData, LoanInput
from typing import List

def generate_snowball_plan(data: FinancialData):
    loans = sorted(data.loans, key=lambda loan: loan.balance)
    return _generate_repayment_schedule(loans, data, method="snowball")

def generate_avalanche_plan(data: FinancialData):
    loans = sorted(data.loans, key=lambda loan: loan.interest_rate, reverse=True)
    return _generate_repayment_schedule(loans, data, method="avalanche")

def _generate_repayment_schedule(loans: List[LoanInput], data: FinancialData, method: str):
    monthly_budget = data.monthly_income
    month = 0
    total_interest = 0.0
    loan_balances = [{**loan.dict()} for loan in loans]

    while any(loan["balance"] > 0 for loan in loan_balances):
        month += 1
        available = monthly_budget
        for loan in loan_balances:
            if loan["balance"] <= 0:
                continue
            interest = (loan["interest_rate"] / 100 / 12) * loan["balance"]
            total_interest += interest
            loan["balance"] += interest
            payment = min(loan["min_payment"], loan["balance"])
            loan["balance"] -= payment
            available -= payment

        for loan in loan_balances:
            if loan["balance"] > 0 and available > 0:
                extra_payment = min(loan["balance"], available)
                loan["balance"] -= extra_payment
                available -= extra_payment
                break

    return {
        "method": method,
        "total_months": month,
        "total_interest_paid": round(total_interest, 2),
        "loans_paid_off": [loan["name"] for loan in loan_balances]
    }
