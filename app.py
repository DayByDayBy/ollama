import ollama
import numpy as np
import streamlit as st


# with st.chat_message("assistant"):
#     st.write("Hello human")
#     st.bar_chart(np.random.randn(30, 3))


response1 = ollama.chat(model='gemma', messages=[
  {
    'role': 'user',
    'content': 'if we do, what shall we want?',
  },
])

response2 = ollama.chat(model='llama2', messages=[
  {
    'role': 'user',
    'content': 'if we do, what shall we want?',
  },
])
# print(response1['message']['content'])
# print(response2['message']['content'])



with st.chat_message("user"):
    st.write({response1['message']['content']})
    
with st.chat_message("admin"):
    st.write({response2['message']['content']})
