from datetime import datetime
import ollama
import streamlit as st
import logging

# logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def get_current_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M")

def generate_responses(model_name, prompt, iterations=10):
    responses = []
    try:
        response = ollama.generate(
            model=model_name,
            prompt=prompt,
            stream=False
        )['response']
        responses.append(response)
        for _ in range(iterations - 1):  # -1 because we already have one response
            response = ollama.generate(
                model=model_name,
                prompt=response,
                stream=False
            )['response']
            responses.append(response)
        logging.info(f"Generated responses for prompt: {prompt[:50]}...")
    except Exception as e:
        logging.error(f"Error during generation: {e}")
    return responses

def main():
    st.title("badChat")
    st.subheader("we never really talk anymore")

    prompts = {
        "prompt_one": {
            "model": "llama3",
            "text": '''tell me something cool, but please don't just wank on about quantum or immortal jellyfish again'''
        },
        "prompt_two": {
            "model": "gemma",
            "text": '''find a cause, and, make a case for it, 
            as passionately as you can. feel free to include 
            examples and citations where necessary'''
        }
    }

    selected_prompt = st.sidebar.selectbox("Select Prompt", list(prompts.keys()))
    model_name = st.sidebar.text_input("Model Name", value=prompts[selected_prompt]["model"])
    iterations = st.sidebar.number_input("Number of Iterations", value=10, min_value=1)

    st.subheader(f"Selected Prompt: {selected_prompt}")
    st.code(prompts[selected_prompt]["text"])

    if st.button('Generate Responses'):
        responses = generate_responses(model_name, prompts[selected_prompt]["text"], iterations)
        for i, response in enumerate(responses):
            st.write(f"Response {i+1}: {response}")
        st.success("Responses generated successfully.")

if __name__ == "__main__":
    main()