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




# def iterator(response):











#     filename = f'./convo/prompt_two_output_{model_name}_{time_stamp}.txt'
    
#     with open(filename, 'w') as file:
#         file.write(responses)
#         for idx, response in enumerate(responses):
#             file.write(f"Response {idx + 1}: {response['response']}\n\n")   


    