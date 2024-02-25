from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_APIKEY'))

model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input,image,prompt):
    response = model.generate_content([input,image[0],prompt])

    return response.text

def input_image_detail(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]

        return image_parts
    else:
        raise FileNotFoundError('No file uploaded')

st.set_page_config(page_title="MultiLanguage Invoice Extractor")

st.header('MultiLanguage Invoice Extractor')
input = st.text_input('Enter your prompt: ',key='input')
uploaded_file = st.file_uploader('Upload an image of invoice', type=['png', 'jpg', 'jpeg'])
image = ''

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

submit = st.button('Tell me about invoice')

input_prompt = """
    You are an expert in understanding invoice. we will upload an image as invoice and you will have to answer any question based on the uploaded invoice image
""" 

if submit:
    image_data = input_image_detail(uploaded_file)
    reponse = get_gemini_response(input_prompt, image_data,input)
    st.subheader('The response is')
    st.write(reponse)