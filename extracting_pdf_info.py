# extracting_pdf_info.py

import os
# import openai
# from dotenv import load_dotenv
import pdfplumber


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
    pdf_file_path = "sample_aid.pdf" # <--- UPDATE THIS WITH YOUR PDF'S FILENAME

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
