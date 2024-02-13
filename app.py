from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM application")
input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit:
    response = model.generate_content(input)
    st.subheader("The respone is")
    st.write(response.text)