import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

# Download Model from https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
def getLLamaresponse(input_text, no_words, blog_style):
    llm = CTransformers(model='.\models\llama-2-7b-chat.ggmlv3.q8_0.bin',
                         model_type='llama', 
                         config={
                             'max_new_tokens':256,
                             "temperature":0.01,})
    
    template = """ 
                Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words.
                """
    
    prompt = PromptTemplate(input_variables=['blog_style', 'input_text', 'no_words'], template=template)

    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))

    return response

st.set_page_config(page_title="Generate Blog", page_icon=":robot:", layout="centered",initial_sidebar_state='collapsed')
st.header("Generate Blogs :robot:")

input_text = st.text_input('Enter the Blog Topic')

col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input('Number of Words')
with col2:
    blog_style = st.selectbox('Write the blog for',('Researches','DataScientist','Common People'),index=0)

submit = st.button('Generate Blog')

if submit:
    st.write(getLLamaresponse(input_text, no_words, blog_style))