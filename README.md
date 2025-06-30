# 🌟 GenAI Greetings App

A simple, elegant Streamlit app to generate friendly greetings using **LangChain + ChatOpenAI**, with full tracing via **LangSmith**.

🔗 **Live Demo**: [hitesh-genai-greetings.streamlit.app](https://hitesh-genai-greetings.streamlit.app/)

---

## ⚙️ What It Does

- 🧠 Uses `ChatOpenAI` to generate AI-powered greetings  
- 🔍 Logs every LLM call to **LangSmith** for observability  
- 💬 Clean UI built in Streamlit  
- 🔐 API keys managed securely using `.env`

---

## 📂 Files

```

├── app.py             # Main Streamlit app
├── .env               # Your secrets (excluded from Git)
├── requirements.txt   # Dependencies
└── .gitignore         # Ignores .env

````

---

## 🚀 Quickstart

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/genai-greeter.git
   cd genai-greeter
   ```

2. **Create a `.env` file**

   ```env
   OPENAI_API_KEY=your-key
   LANGCHAIN_API_KEY=your-langsmith-key
   LANGCHAIN_PROJECT=GenAI Beginner Track
   LANGCHAIN_TRACING_V2=true
   ```

3. **Install & Run**

   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```

---

## 🧪 Tech Stack

* 💬 [LangChain](https://www.langchain.com/)
* 🤖 [OpenAI Chat Models](https://platform.openai.com/)
* 📊 [LangSmith](https://smith.langchain.com/)
* 🖼️ [Streamlit](https://streamlit.io/)

---

## 👨‍💻 Author

Made by [Hitesh](https://hitesh-genai-greetings.streamlit.app/)