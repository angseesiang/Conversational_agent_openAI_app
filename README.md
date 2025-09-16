# 🤖 Conversational Agent (OpenAI API + Flask)

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](#)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-green)](#)
[![Flask](https://img.shields.io/badge/Flask-lightgrey)](#)
[![Pytest](https://img.shields.io/badge/Tested-Pytest-orange)](#)

This project implements a **conversational AI chatbot** powered by the OpenAI API (GPT-4o).  
It includes a Flask web interface, simple styling, and unit tests for validation.

---

## 📖 Contents

- `agent.py` – Core implementation of the conversational agent  
- `app.py` – Flask application serving chatbot responses  
- `index.html` & `styles.css` – Frontend UI for user interaction  
- `.env` – Stores your **OpenAI API key**  
- `test_agent.py` – Unit tests for the chatbot  
- `requirements.txt` – Project dependencies  
- `url.txt` – Repository reference  

---

## 🚀 How to Use

### 1) Clone this repository

```bash
git clone https://github.com/angseesiang/Conversational_agent_openAI_app.git
cd Conversational_agent_openAI_app
```

### 2) Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # On Linux / macOS
venv\Scripts\activate      # On Windows
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Configure your OpenAI API key

Create a `.env` file in the project root and add:

```env
OPENAI_API_KEY=your_api_key_here
```

### 5) Start the Flask application

```bash
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser and interact with the chatbot.

### 6) Run unit tests

```bash
pytest test_agent.py
```

This will validate that the chatbot generates responses and handles parameters correctly.

### 7) Open in Google Colab (optional)

After uploading this repository to GitHub, you can run it directly in  
[Google Colab](https://colab.research.google.com) without local setup.  

Use the following link format:

```
https://colab.research.google.com/github/<your-username>/<your-repo-name>/blob/main/<notebook>.ipynb
```

Replace `<your-username>`, `<your-repo-name>`, and `<notebook>` with your details.  
For example, if you create `chatbot_demo.ipynb`, you can open it directly in Colab to test the chatbot in the cloud.

---

## 🛠️ Requirements

- Python 3.9+  
- OpenAI  
- Flask  
- Joblib  
- Pytest  
- Python-dotenv  

All dependencies are listed in `requirements.txt`.

---

## 📌 Notes

- The agent uses **OpenAI GPT-4o** by default.  
- Ensure your `.env` file contains a valid API key.  
- Unit tests confirm response generation and parameter handling.  

---

## 📜 License

This project is for **educational purposes only**.
