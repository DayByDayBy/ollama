from datetime import datetime  

import ollama
import streamlit as st

time_stamp = datetime.now().strftime("%Y%m%d_%H%M")
model_name = "gemma"
iterations = 10
prompt_two = '''\n\n find a cause, and, 
make a case for it, as passionately as you 
can. feel free to include examples and 
citations where necessary'''


responses = []

def generate_one(prompt_two):
    try:
        response = ollama.generate(
            model = model_name,
            prompt = prompt_two,
            stream = False
        )['response']
        responses.append(response)
        for _ in range(iterations): 
            response = ollama.generate(
                model = model_name,
                prompt = response,
                stream = False
            )['response']
            responses.append(response)
            
        st.success("Responses generated successfully.")
        st.write(responses) 
    except Exception as e:  
        st.error(f"Error during generation: {e}")    

def main():
    st.title("badChat")
    st.subheader("we never really talk anymore")

    st.code(prompt_two)
    if st.button('convo one'):
        generate_one(prompt_two)

if __name__ == "__main__":
    main()







# def iterator(response):











#     filename = f'./convo/prompt_two_output_{model_name}_{time_stamp}.txt'
    



#     with open(filename, 'w') as file:
#         file.write(responses)
#         for idx, response in enumerate(responses):
#             file.write(f"Response {idx + 1}: {response['response']}\n\n")     