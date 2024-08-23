#Basic langchain using llama2 and streamlit

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama


import os
import streamlit as st


from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate(
    [
        ("system","You are a helpfull assistant. Please response to user queries"),
        ("user","Question: {question}")
    ]
)

st.title("Langchain Demo App")
input_text = st.text_input("Search the topic u want..")

llm = Ollama(model="moondream")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({"question":input_text}))
