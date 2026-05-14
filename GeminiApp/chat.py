from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from google import genai

# Load API key
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize client
client = genai.Client(api_key=api_key)

def get_gemini_response(question):
    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=question
    )
    return response.text


# Streamlit UI
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")

user_input = st.text_input("Input:", key="input")

submit = st.button("Ask the question")

if submit and user_input:
    response = get_gemini_response(user_input)

    st.subheader("The Response is")
    st.write(response)

    