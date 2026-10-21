# 📄 AI Document Analyzer

An AI-powered web application built with **Python, Streamlit, and Google Gemini API** to analyze and compare two PDF documents. It identifies similarities, differences, and key information, and generates a downloadable comparison report.

## ✨ Features

- **PDF Text Extraction:** Extracts text from PDF documents using `pypdf`.
- **AI-Powered Comparison:** Uses Google Gemini to identify similarities, differences, and important details.
- **Interactive Interface:** Simple and user-friendly web interface built with Streamlit.
- **Report Export:** Downloads the comparison results as a Microsoft Word (`.docx`) document.

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API (`google-genai`)
- pypdf
- python-docx
- python-dotenv

## 📂 Project Structure

```text
ai-document-analyzer/
├── app.py                 # Main Streamlit application
├── document_reader.py     # PDF text extraction
├── comparison.py          # AI comparison logic
├── report_generator.py    # Word report generation
├── requirements.txt       # Project dependencies
├── .env                   # API key configuration
├── .gitignore             # Git exclusions
└── README.md
```

## 🚀 Installation and Usage

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/ai-document-analyzer.git
cd ai-document-analyzer
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Configure your API key**

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Get your API key from [Google AI Studio](https://aistudio.google.com/).

**4. Run the application**

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to use the application.

## ⚠️ Note

AI-generated results may contain errors. Always verify important findings against the original documents. Never commit your `.env` file or expose your API key on GitHub.

## 👨‍💻 Author

**GUNAVARDHINI ATHURU** — [GitHub](https://github.com/Gunavardhini2006)
