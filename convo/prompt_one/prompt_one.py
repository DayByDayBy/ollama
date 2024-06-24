from datetime import datetime  

import ollama
import streamlit as st


time_stamp = datetime.now().strftime("%Y%m%d_%H%M")
model_name = "llama3"
iterations = 10
prompt_one = '''tell me something cool, 
        but please don\'t just wank on about 
        quantum or immortal jellyfish again'''


responses = []

def generate_one(prompt_one):
    try:
        response = ollama.generate(
            model = model_name,
            prompt = prompt_one,
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


    st.code(prompt_one)
    if st.button('convo one'):
        generate_one(prompt_one)




if __name__ == "__main__":
    main()




# def iterator(response):











#     filename = f'./convo/prompt_one_output_{model_name}_{time_stamp}.txt'
    



#     with open(filename, 'w') as file:
#         file.write(responses)
#         for idx, response in enumerate(responses):
#             file.write(f"Response {idx + 1}: {response['response']}\n\n")     