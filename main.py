from fastapi import FastAPI
from routing_url import router

app = FastAPI(title="Loan Repayment Planner")
app.include_router(router)
