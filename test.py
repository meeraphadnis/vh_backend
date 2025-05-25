from google import genai
import convert_pdf_png
from PIL import Image
import io

with open("gemini_api_key", "r") as f:
    gemini_api_key_variable = f.read()
client = genai.Client(api_key=gemini_api_key_variable)

finances_text_path = "extracted_pdf_content.txt"
with open(finances_text_path, "r", encoding="utf-8") as file:
    extracted_result = file.read()


response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents= f"Print out the contents of this file: {extracted_result}"
)

response_two = client.models.generate_content(
    model="gemini-2.0-flash",
    contents= f"Return the numbers with a dollar sign in front of them and what that number means: {extracted_result}" 
)


response_three = client.models.generate_content(
    model="gemini-2.0-flash",
    contents= f"Only return back the information from the table: {response_two}" 
)

with open("page_converted.png", "rb") as f:
    extracted_image = f.read()

response_four = client.models.generate_content(
    model="gemini-1.5-flash",
    contents= f"Return all the numbers within the image: {extracted_image}" 
)

'''
if response is None or not response.contents:
    print("No response received or response is empty.")
else:
    print("\n Illustrative Example of Standard Repayment Plan:")
    print(response.text)
'''

#print(response_two.text)
# print(response_three.text)
print(response_four.text)