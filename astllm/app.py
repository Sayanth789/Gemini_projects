import streamlit as st
from google import genai 
import os 
import PyPDF2 as pdf 
from dotenv import load_dotenv 
import json 


load_dotenv() 
print(os.getenv("GOOGLE_API_KEY"))


client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(prompt):

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

# Prompt Template 
input_prompt = """


Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science,data analyst
and big data engineer.

Your task is to evaluate the resume based on the given job description.

resume:{text}
description:{jd}

I want the response in one single string having the structure

{{"JD Match":"%","MissingKeywords":[],"Profile Summary":""}}

"""


# Streamlit app 
st.markdown("*This is a test* **App**")
st.title("`Smart ATS`")
st.text("Imporve Your Resumt ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")


submit = st.button("submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)

        final_prompt = input_prompt.format(

            text=text,
            jd=jd
        )
        response=get_gemini_response(input_prompt)
        st.subheader("The Response")
        st.subheader(response)