import streamlit as st
import ollama
from datetime import datetime

iterations = 10
model_one_name = "llama3"
model_two_name = "gemma"

prompt_one = '''tell me something cool, 
but please don't just wank on about 
quantum or immortal jellyfish again'''
prompt_two = '''find a cause, and, 
make a case for it, as passionately as you 
can. feel free to include examples and 
citations where necessary'''

def generate_responses(model_name, prompt, iterations):
    responses = []
    try:
        response = ollama.generate(model=model_name, prompt=prompt, stream=False)['response']
        responses.append(response)
        for _ in range(iterations - 1): 
            response = ollama.generate(model=model_name, prompt=response, stream=False)['response']
            responses.append(response)
    except Exception as e:
        st.error(f"Error during generation: {e}")
    return responses

def automated_chat(responses, model_name):
    conversation = []
    for msg in responses:
        try:
            response = ollama.chat(model=model_name, messages=[{'role': 'user', 'content': msg}])
            conversation.append((msg, response['message']['content']))
        except Exception as e:
            st.error(f"Error during chat: {e}")
    return conversation

# Streamlit UI
def main():
    st.title("badChat")
    st.subheader("We never really talk anymore")

    if st.button('Start Conversation One'):
        responses = generate_responses(model_one_name, prompt_one, iterations)
        conversation = automated_chat(responses, model_two_name)
        for user_msg, model_reply in conversation:
            st.write(f"User: {user_msg}")
            st.write(f"Model: {model_reply}")

    if st.button('Start Conversation Two'):
        responses = generate_responses(model_two_name, prompt_two, iterations)
        conversation = automated_chat(responses, model_one_name)
        for user_msg, model_reply in conversation:
            st.write(f"User: {user_msg}")
            st.write(f"Model: {model_reply}")

if __name__ == "__main__":
    main()
