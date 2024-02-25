from langchain.llms import OpenAI 
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def get_openai_response(question):
    llm = OpenAI(temperature=0.5)
    response = llm(question)

    return response

st.set_page_config(page_title="Ask AI", page_icon=":robot:")
st.header('LangChain Application')

input = st.text_input('Input: ',key='input')
response = get_openai_response(input)

submit = st.button('Ask the question')
if submit:
    st.subheader('The response is')
    st.write(response)
