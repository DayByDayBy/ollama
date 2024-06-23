from datetime import datetime  

import ollama
import streamlit as st


time_stamp = datetime.now().strftime("%Y%m%d_%H%M")
model_name = "llama3"
prompt_two = '''teach me about a neat trick i 
        can share with friends but make 
        sure it's kid friendly this time'''


response = ollama.generate(
    model = model_name,
    prompt = prompt_two,
    stream = False
)['response']

print(response)



    