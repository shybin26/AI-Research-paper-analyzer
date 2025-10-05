import fitz  # PyMuPDF
import google.generativeai as genai
import os  # <-- NEW: Import the os library

# --- CONFIGURATION ---
# PASTE YOUR GOOGLE AI API KEY HERE
GOOGLE_API_KEY = 'AIzaSyB90kC8N03pwrQlUWmyWDoNZ8U8R6L0SiE'

genai.configure(api_key=GOOGLE_API_KEY)

def read_pdf_text(filename):
    """A function to read the text from a PDF file."""
    try:
        doc = fitz.open(filename)
        full_text = ""
        for page in doc:
            full_text += page.get_text()
        doc.close()
        return full_text
    except Exception as e:
        return f"Error: Could not read file '{filename}'. Reason: {e}"

def summarize_with_ai(text_to_summarize):
    """Uses the Gemini model to summarize the provided text."""
    if not text_to_summarize:
        return "Error: No text provided to summarize."

    print("🤖 Contacting the AI model... This might take a moment...")

    try:
        model = genai.GenerativeModel('models/gemini-2.5-flash-lite')
        prompt = "Summarize the following research paper text. Focus on the key findings, methodology, and conclusion. Provide a concise summary:"
        response = model.generate_content(prompt + "\n\n" + text_to_summarize)
        return response.text
    except Exception as e:
        return f"Error: AI summarization failed. Reason: {e}"

# --- The New Main Logic Starts Here ---

# 1. Get a list of all files in the current directory
all_files = os.listdir('.')

# 2. Filter this list to find only the PDF files
pdf_files = [file for file in all_files if file.endswith(".pdf")]

# 3. Check if any PDFs were found
if not pdf_files:
    print("❌ No PDF files found in this folder. Please add some PDFs and try again.")
else:
    print(f"✅ Found {len(pdf_files)} PDF(s) to analyze.")

    # 4. Loop through each PDF file
    for pdf_filename in pdf_files:
        print(f"\n\n--- 📄 Processing: {pdf_filename} ---")

        # Read the text from the current PDF
        extracted_text = read_pdf_text(pdf_filename)

        # If reading was successful, summarize it
        if "Error:" not in extracted_text:
            ai_summary = summarize_with_ai(extracted_text)
            print("\n--- 🧠 AI Summary ---")
            print(ai_summary)
        else:
            # If reading failed, print the error
            print(f"❌ {extracted_text}")

print("\n\n--- ✅ All files processed. ---")