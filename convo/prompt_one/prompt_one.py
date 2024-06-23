from datetime import datetime  

import ollama
import streamlit as st


time_stamp = datetime.now().strftime("%Y%m%d_%H%M")
model_name = "llama3"
prompt_one = '''tell me something cool, 
        but please don\'t just wank on about 
        quantum or immortal jellyfish again'''


response = ollama.generate(
    model = model_name,
    prompt = prompt_one,
    stream = False
)['response']

print(response)
