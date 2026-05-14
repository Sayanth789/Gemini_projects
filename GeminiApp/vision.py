# vision.py file
from dotenv import load_dotenv

load_dotenv()

import streamlit as st 
import os 
import pathlib
import textwrap
from PIL import Image 

from google import genai 

api_key = os.getenv('GOOGLE_API_KEY')

client =  genai.Client(api_key=api_key)


def get_gemini_response(prompt,image):
    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        content=[prompt, image]
    )
    return response.text



# Initializing the streamlit app 

st.set_page_config(page_title="Gemini Image Demo")


st.header("Gemini Vision Application")

input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image.. ",  type=["jpg", "jpeg", "png"])

image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell Me About The Image")    

if submit and image is not None:
    repsonse = get_gemini_response(input, image)
    st.subheader("The Response is")
    st.write(repsonse)