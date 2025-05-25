from google import genai
import convert_pdf_png
#import requests


with open("gemini_api_key", "r") as f:
    gemini_api_key_variable = f.read()
client = genai.Client(api_key=gemini_api_key_variable)

finances_text_path = "extracted_pdf_content.txt"
with open(finances_text_path, "r", encoding="utf-8") as file:
    extracted_result = file.read()


response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents= f"Find the total cost of financial aid given from this file: {extracted_result}"
)

# response_two = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents= f"Return the numbers with a dollar sign in front of them and what that number means: {extracted_result}" 
# )

# response_three = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents= f"Only return back the information from the table: {response_two}" 
# )


# my_image = client.files.upload(file = "page_converted.png")

# response_four = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents=[my_image, "Return the numbers from this image."],
# )

print(response.text)
# print(response_two.text)
# print(response_three.text)
# print(response_four.text)
