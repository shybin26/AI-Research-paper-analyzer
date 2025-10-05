from flask import Flask, render_template, request, jsonify
import fitz
import google.generativeai as genai

# --- CONFIGURATION ---
GOOGLE_API_KEY = 'AIzaSyB90kC8N03pwrQlUWmyWDoNZ8U8R6L0SiE'
genai.configure(api_key=GOOGLE_API_KEY)
app = Flask(__name__)

# --- PDF Reading Function (no changes) ---
def read_pdf_text(file_stream):
    try:
        doc = fitz.open(stream=file_stream, filetype="pdf")
        full_text = "".join(page.get_text() for page in doc)
        doc.close()
        return full_text
    except Exception as e:
        return f"Error reading PDF: This may not be a valid PDF file."

# --- NEW: More Powerful AI Function ---
def perform_ai_analysis(text_to_analyze, action):
    if not text_to_analyze or "Error:" in text_to_analyze:
        return {"error": text_to_analyze}
    
    # Define the prompts for each action
    prompts = {
        "summarize": "Summarize the following research paper text. Focus on the key findings, methodology, and conclusion.",
        "extract_terms": "Extract and list the key terms, concepts, and keywords from the following research paper text. Separate them with commas.",
        "identify_methodology": "Identify and describe the methodology used in the following research paper. Be specific about the techniques, tools, and processes mentioned."
    }

    # Define the titles for the results
    titles = {
        "summarize": "Summary",
        "extract_terms": "Key Terms",
        "identify_methodology": "Methodology"
    }

    prompt_text = prompts.get(action, "Summarize the following text:") # Default to summarize
    result_title = titles.get(action, "Result")

    try:
        model = genai.GenerativeModel('models/gemini-2.5-flash-lite') # Or your working model
        response = model.generate_content(prompt_text + "\n\n" + text_to_analyze)
        return {"title": result_title, "result": response.text}
    except Exception as e:
        return {"error": f"Error with AI analysis: {e}"}

# --- WEB ROUTES ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_route():
    if 'pdf_file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['pdf_file']
    action = request.form.get('action', 'summarize') # Get the action from the form

    if file.filename == '' or not file.filename.lower().endswith('.pdf'):
        return jsonify({'error': 'Please upload a valid PDF file.'}), 400
        
    pdf_text = read_pdf_text(file.stream.read())
    result = perform_ai_analysis(pdf_text, action)
    
    if "error" in result:
        return jsonify(result), 400
    else:
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)