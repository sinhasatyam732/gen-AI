import streamlit as st
from langchain_groq import ChatGroq


lim = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    groq_api_key="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"

)

st.circle("Simple LLM ChatBot")
st.write("enter your query below")
user_input = st.text_input("Your Quiestion:")


if st.button("Get Answer");
    response = llm.invoke(user_input)
    st.write(### response)
        st,write(response)