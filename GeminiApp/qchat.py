from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from google import genai

api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

# Function
def get_gemini_response(question):
    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=question
    )
    return response.text



# Streamlit UI
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

user_input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

if submit and user_input:
    response = get_gemini_response(user_input)

    st.session_state["chat_history"].append(("You", user_input))
    st.session_state["chat_history"].append(("Bot", response))

    st.subheader("The response is")
    st.write(response)

st.subheader("Chat history")

for role, text in st.session_state["chat_history"]:
    st.write(f"{role}: {text}")