from dotenv import load_dotenv
load_dotenv()
import streamlit as st 
import os 
from PIL import Image 
from google import genai 

api_key = os.environ['GOOGLE_API_KEY']

client = genai.Client()


def get_gemini_response(input_text, image, user_prompt):

    response = client.models.generate_content(  
        model= "models/gemini-2.5-flash",
        contents=[
            input_text,
            image[0],
            user_prompt

        ]
    )
   
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mimi_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded")
    

##initialize our streamlit app

st.set_page_config(page_title="MultiLanguage Invoice Extractor")

st.header("MultiLanguage Invoice Extractor")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Tell me about the invoice")

input_prompt = """

You are an expert in understanding invoices. We will upload a a image as invoice
and you will have to answer any questions based on the uploaded invoice image

"""
# If submit button is clicked 

if submit:
    image_data = input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt, image_data, input)
    st.subheader("The Response is")
    st.write(response)