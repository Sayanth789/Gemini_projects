# app.py file
from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os 
import pathlib
import textwrap

from google import genai 

# from IPython.display import display,Markdown 
# It only work in jupyter notebook so we don't need it, then why is it there
# for a remark  ...! 


def to_markdown(text):
    text = text.replace("•", " *")
    return textwrap.indent(text, "> ")

os.getenv('GOOGLE_API_KEY')

# Function to load OpenAI model and get responses
client = genai.Client()

def get_gemini_response(question):

    response = client.models.generate_content(  
        model= "models/gemini-2.5-flash",
        contents=question
    )
   
    return response.text

# Initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")

input = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# If ask button is clicked `boy`

if submit:

    response = get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)

    