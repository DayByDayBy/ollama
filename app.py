import ollama
# import nlu
import numpy as np
import streamlit as st
# import matplotlib.pyplot as plt

    
prompt  = 'if we do, what shall we want?'

prompt2 = 'write an interesting prompt for an LLM. it should be framed as a request for an interesting prompt'
prompt3 = 'as a prompt engineer, write an interesting prompt for an LLM. it should be framed as a request for an interesting prompt'


# # with st.chat_message("assistant"):
# #     st.write("Hello human")
# #     st.bar_chart(np.random.randn(30, 3))


response1 = ollama.chat(
    model='gemma', 
    messages=[
    {
    'role': 'user',
    'content': prompt2,
    },
])

response2 = ollama.chat(
    model='llama2', 
    messages=[
    {
    'role': 'user',
    'content': prompt2,
    },
])

# with st.chat_message("user"):
#     st.write(response1['message']['content'])
    
# with st.chat_message("admin"):
#     st.write(response2['message']['content'])

# nlu.load('sentiment').predict('I love NLU! <3') 

col1, col2, col3 = st.columns([3, 5, 5])
with col2:
    st.write(response1['message']['content'])
with col3:
    st.write(response2['message']['content'])
    
    
