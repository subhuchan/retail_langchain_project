import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.title("AtliQ T Shirts: Database Q&A")

question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()
    response = chain.invoke(question)
    
    st.header("Answer")
    # Handle both dict response and string response
    if isinstance(response, dict):
        st.write(response.get("result", response))
    else:
        st.write(response)

