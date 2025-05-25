from google import genai


with open("gemini_api_key", "r") as f:
    gemini_api_key_variable = f.read()

client = genai.Client(api_key=gemini_api_key_variable)

# finances_text_path = "extracted_pdf_content.txt"
# with open(finances_text_path, "r", encoding="utf-8") as file:
#     extracted_result = file.read()


def find_financial_aid_cost(text):
    finances_text_path = text
    with open(finances_text_path, "r", encoding="utf-8") as file:
        extracted_result = file.read()
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents= f"Find the total cost of financial aid given from this file: {text}"
    )
    return response.text


print(find_financial_aid_cost("extracted_pdf_content.txt"))
# print(response.text)
# print(response_two.text)
# print(response_three.text)
# print(response_four.text)
