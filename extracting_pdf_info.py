# extracting_pdf_info.py

import os
# import openai
# from dotenv import load_dotenv
import pdfplumber

# load_dotenv()

# def extract_financial_data_from_text(text: str) -> dict:
#     prompt = f"""
#     Extract the following from this financial aid document and return JSON:
#     - Tuition and fees
#     - Room and board
#     - Transportation
#     - Personal expenses
#     - Total cost of attendance
#     - Loan limits by grade level and type (subsidized/unsubsidized)

#     PDF Text:
#     {text}
#     """

#     openai.api_key = os.getenv("OPENAI_API_KEY")
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[
#             {"role": "system", "content": "You are a financial data extractor."},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.2,
#         max_tokens=1000
#     )

#     return response.choices[0].message["content"].strip()
#     content_str = response.choices[0].message["content"].strip()
#     try:
#         return json.loads(content_str)
#     except json.JSONDecodeError:
#         raise ValueError(f"Failed to parse JSON from OpenAI response: {content_str}")


# import pdfplumber


# def convert_pdf_to_text(pdf_path: str, output_txt_path: str) -> None:
#     """
#     Extracts all text from a PDF file and saves it to a .txt file.

#     Args:
#         pdf_path (str): The path to the input PDF file.
#         output_txt_path (str): The path where the extracted text will be saved.
#     """
#     try:
#         all_text = ""
#         with pdfplumber.open(pdf_path) as pdf:
#             for page in pdf.pages:
#                 # Extract text from the current page
#                 page_text = page.extract_text()
#                 if page_text: # Ensure there's text to add
#                     all_text += page_text + "\n" # Add a newline between pages

#         # Save the extracted text to a .txt file
#         with open(output_txt_path, "w", encoding="utf-8") as f:
#             f.write(all_text)

#         print(f"Successfully extracted text from '{pdf_path}' to '{output_txt_path}'")

#     except pdfplumber.PdfError as e:
#         print(f"Error processing PDF file '{pdf_path}': {e}")
#     except FileNotFoundError:
#         print(f"Error: PDF file not found at '{pdf_path}'")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# # --- Example Usage ---
# if __name__ == "__main__":
#     # 1. Create a dummy PDF for testing (if you don't have one)
#     # For simplicity, you can manually create a small PDF or download a sample.
#     # Let's assume you have a PDF named 'sample.pdf' in the same directory
#     # as your script, or you can provide a full path.
#     input_pdf_file = "testerfile.pdf"
#     output_text_file = "output_from_testerfile.txt"


#     # Create a dummy PDF (requires reportlab, often used for PDF generation)
#     # If you don't have reportlab, just make sure to place a 'sample.pdf'
#     # in the same directory as this script.
#     '''
#     try:
#         from reportlab.pdfgen import canvas
#         from reportlab.lib.pagesizes import letter

#         c = canvas.Canvas(input_pdf_file, pagesize=letter)
#         c.drawString(100, 750, "This is the first line of text on page 1.")
#         c.drawString(100, 730, "And here's some more text.")
#         c.showPage() # Start a new page
#         c.drawString(100, 750, "Text on page 2 starts here.")
#         c.save()
#         print(f"Created dummy PDF: {input_pdf_file}")
#     except ImportError:
#         print("reportlab not installed. Please ensure 'sample.pdf' exists for testing.")
#         print("You can install it with: pip install reportlab")
#     except Exception as e:
#         print(f"Could not create dummy PDF: {e}")
#     '''

#     # Now, run the conversion
#     if os.path.exists(input_pdf_file):
#         convert_pdf_to_text(input_pdf_file, output_text_file)
#     else:
#         print(f"Skipping conversion: '{input_pdf_file}' not found.")

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts all text from a PDF file.

    Args:
        pdf_path (str): The path to the input PDF file.

    Returns:
        str: The extracted text from the PDF, or an empty string if an error occurs.
    """
    all_text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    all_text += page_text + "\n"
    except pdfplumber.PdfError as e:
        print(f"Error processing PDF file '{pdf_path}': {e}")
        return "" # Return empty string on error
    except FileNotFoundError:
        print(f"Error: PDF file not found at '{pdf_path}'")
        return ""
    except Exception as e:
        print(f"An unexpected error occurred during PDF text extraction: {e}")
        return ""
    return all_text.strip()


# --- Main execution block for testing PDF to Text only ---
if __name__ == "__main__":
    # --- IMPORTANT: Configure your PDF file here ---
    # Replace 'your_actual_financial_aid_document.pdf' with the actual name of YOUR PDF file.
    # Make sure this PDF file is in the same directory as this script.
    pdf_file_path = "sample-aid.pdf" # <--- UPDATE THIS WITH YOUR PDF'S FILENAME

    # This is the path where the extracted text will be saved.
    output_text_file_path = "extracted_pdf_content.txt"

    print("Starting PDF to Text Extraction")
    print("1. Attempting to extract text from:", pdf_file_path)

    # Extract text from the PDF
    pdf_text = extract_text_from_pdf(pdf_file_path)
    print("text from file", pdf_text)

    if pdf_text:
        # Save the extracted text to a file
        try:
            with open(output_text_file_path, "w", encoding="utf-8") as f:
                f.write(pdf_text)
            print(f"2. Successfully extracted text and saved to: {output_text_file_path}")
            print(f"You can now open '{output_text_file_path}' to review the extracted content.")
        except Exception as e:
            print(f"2. Error saving extracted text to file: {e}")
            print(f"\n--- ❌ Extraction Failed at Saving ---")
    else:
        print("\n--- ❌ PDF Text Extraction Failed ❌ ---")
        print("Could not extract text from the PDF. Please ensure the PDF path is correct,")
        print("the file exists, and it contains readable text.")
