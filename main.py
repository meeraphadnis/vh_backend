# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routing_url import router

app = FastAPI(title="Loan Repayment Planner")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)
app.include_router(router)

