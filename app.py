from langchain_openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
from langchain.globals import set_debug


load_dotenv()

#To see debug details in question-answers set to "True"
set_debug(False)

def get_answer(question):
    llm= OpenAI(model_name="gpt-3.5-turbo-instruct")
    answer = llm.invoke(question)
    return answer

def get_question():
    user_question = st.text_input("Escreva sua Pergunta:", key="input")
    return user_question

## Application page title
title = "Everything🧠"
st.set_page_config(page_title=title, page_icon=":robot:")
st.header(title+" - 'Aquele que Tudo Sabe'💫")


user_question = get_question()
answer = get_answer(user_question)

submit = st.button("Fazer Pergunta")
if submit:
    st.subheader("Resposta:")
    st.write(answer)