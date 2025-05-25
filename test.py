from google import genai

with open("gemini_api_key", "r") as f:
    gemini_api_key_variable = f.read()
client = genai.Client(api_key=gemini_api_key_variable)

prompt_for_response = """
Consider a **hypothetical** student with a total federal student loan principal of $30,000 at a fixed interest rate of 4.5%. Their current annual gross income is $40,000.

For **illustrative purposes only**, describe what a "Standard Repayment Plan" might look like for this hypothetical student, including:
- The typical term length for a federal standard plan.
- A **general estimate** of the monthly payment (e.g., using a simple amortization calculation formula, but state it's an estimate).
- The total estimated interest paid over the life of the loan.

**CRITICAL DISCLAIMER:** This is a purely illustrative example based on general assumptions and NOT financial advice. 
Actual loan payments depend on many factors including exact loan terms, lender policies, and individual financial situations. 
Students should consult a qualified financial advisor or their loan servicer for accurate, personalized information and guidance.
Do NOT make financial decisions based on this hypothetical output.
"""

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents= prompt_for_response
)

if response is None or not response.contents:
    print("No response received or response is empty.")
else:
    print("\n Illustrative Example of Standard Repayment Plan:")
    print(response.text)
