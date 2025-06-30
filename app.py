import streamlit as st
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Load API keys from .env
load_dotenv()

# Streamlit UI
st.title("🤖 LangChain Greeter with LangSmith")
st.write("Enter a name and get a friendly greeting from ChatOpenAI!")

# Input box
user_name = st.text_input("Your name:")

if st.button("Greet Me") and user_name:
    # Create message
    prompt = f"Say a friendly greeting to a user named {user_name}"
    message = HumanMessage(content=prompt)

    # LangChain LLM
    llm = ChatOpenAI(model_name="gpt-3.5-turbo-16k", temperature=0)
    response = llm([message])

    # Output
    st.success(response.content)