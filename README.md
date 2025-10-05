 🧠 AI Research Paper Analyzer

A web-based application that leverages the power of Large Language Models to help students, academics, and researchers quickly analyze, summarize, and understand complex research papers. This tool allows users to upload a PDF and receive instant, AI-powered insights without leaving their browser.



---
## ✨ Key Features

* **PDF Upload:** A simple and intuitive web interface for uploading research papers in `.pdf` format.
* **Instant Summarization:** Get a concise summary of any research paper, focusing on its core findings, methodology, and conclusions.
* **Advanced AI Analysis:** Go beyond summarization with more specific analysis options:
    * **Extract Key Terms:** Automatically identify and list the most important terms and concepts.
    * **Identify Methodology:** Get a clear description of the research methods used in the paper.
* **Modern User Experience:** A sleek, single-page application that provides results without needing to reload the page, complete with a loading indicator and user-friendly error handling.

---
## 🛠️ Technology Stack

This project is built with a modern, Python-based web stack.

* **Backend:**
    * **Flask:** A lightweight Python web framework for serving the application.
    * **Google Gemini API:** The powerful AI model used for all text analysis and summarization tasks.
    * **PyMuPDF (Fitz):** A robust library for extracting text content from PDF files.
* **Frontend:**
    * **HTML5 & CSS3:** For the structure and basic styling of the application.
    * **Bootstrap 5:** A professional CSS framework for building a responsive and modern user interface.
    * **JavaScript (Fetch API):** To handle asynchronous form submissions (AJAX), providing a smooth, no-reload user experience.

---
## 🚀 Setup and Usage

To run this project on your local machine, follow these steps:

### **Prerequisites**

* Python 3.8+
* pip (Python package installer)
* A Google AI API Key

### **1. Clone the Repository**

```bash
git clone [https://github.com/your-username/ai-paper-analyzer.git](https://github.com/your-username/ai-paper-analyzer.git)
cd ai-paper-analyzer
