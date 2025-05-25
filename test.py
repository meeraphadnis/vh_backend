from google import genai

with open("gemini_api_key", "r") as f:
    gemini_api_key_variable = f.read()
client = genai.Client(api_key=gemini_api_key_variable)


response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="what is the capital of california?"
)

print(response.text)
