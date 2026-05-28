# 🚀 FactCheck Pro  
### AI-Powered Fact Verification & Claim Analysis System

FactCheck Pro is an AI-driven web application that automatically extracts claims from PDF documents or text input and verifies them using Large Language Models (LLMs) and real-time web intelligence.

The platform classifies claims into:

- ✅ Verified  
- ⚠️ Inaccurate  
- ❌ False  

along with confidence scores and detailed explanations.

---

## 📌 Features

✨ Upload PDF files for automatic claim extraction  
✨ AI-powered fact verification using Gemini API  
✨ Real-time claim validation  
✨ Smart classification system  
✨ Downloadable verification reports  
✨ Clean and responsive Streamlit interface  
✨ Modular backend architecture  
✨ Easy deployment using Streamlit Cloud  

---

## 🖼️ Application Workflow

```text
PDF/Text Input
       ↓
Claim Extraction
       ↓
AI Fact Verification
       ↓
Classification
       ↓
Report Generation
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Backend |
| Streamlit | Frontend Web App |
| Gemini API | AI Fact Verification |
| BeautifulSoup | Web Scraping |
| Requests | API Handling |
| PyMuPDF | PDF Text Extraction |
| Pandas | Data Processing |

---

# 📂 Project Structure

```bash
factcheck-pro/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── modules/
│   ├── pdf_extractor.py
│   ├── claim_extractor.py
│   ├── fact_checker.py
│   ├── report_generator.py
│   └── utils.py
│
├── assets/
│   └── styles.css
│
└── exports/
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/factcheck-pro.git
cd factcheck-pro
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

---

# 🔑 Generate Gemini API Key

Visit:

👉 https://makersuite.google.com/app/apikey

Generate your API key and paste it into the `.env` file.

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Application will start on:

```text
http://localhost:8501
```

---

# ☁️ Deployment

This project can be deployed easily using Streamlit Community Cloud.

## 🔗 Streamlit Deployment

👉 https://factcheck-pro-e5wwz2ssjhf4rtdhdsafld.streamlit.app/

### Deployment Steps

1. Push project to GitHub
2. Login to Streamlit Cloud
3. Select repository
4. Set:
   - Branch → `main`
   - Main File → `app.py`
5. Add Streamlit Secrets:

```toml
GEMINI_API_KEY="your_api_key_here"
```

6. Click Deploy 🚀

---

# 📊 Output Categories

| Status | Description |
|--------|-------------|
| ✅ Verified | Claim is factually correct |
| ⚠️ Inaccurate | Claim contains partial inaccuracies |
| ❌ False | Claim is incorrect or misleading |

---

# 📸 Screenshots

## Home Interface

_Add application screenshots here_

```md
![Homepage](assets/screenshot1.png)
```

---

# 🔒 Security Notes

⚠️ Never expose your API keys publicly.

Add `.env` inside `.gitignore`

```gitignore
.env
__pycache__/
```

---

# 🚀 Future Improvements

- 🌍 Multi-language Support  
- 🎙️ Voice-based Fact Verification  
- 📈 Advanced Credibility Scoring  
- 📰 Live News Monitoring  
- 🧠 Improved AI Reasoning  
- 🌐 Browser Extension Support  

---

# 👨‍💻 Author

## Aman Mishra

Management Trainee – Product Management Assignment

---

# 📜 License

This project is developed for educational and assessment purposes only.

---

# ⭐ Acknowledgement

Special thanks to:
- Google Gemini API
- Streamlit
- Open Source Python Community

---

# 💡 Support

If you found this project useful, consider giving it a ⭐ on GitHub.
