from datetime import datetime
import ollama
import streamlit as st
import logging

# logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def get_current_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M")

def generate_responses(model_name, prompts, iterations=10):
    all_responses = []
    for prompt in prompts:
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
            all_responses.append(responses)
            logging.info(f"Generated responses for prompt: {prompt[:50]}...")
        except Exception as e:
            logging.error(f"Error during generation: {e}")
    return all_responses

def main():
    st.title("badChat")
    st.subheader("we never really talk anymore")

    model_name = st.sidebar.text_input("Model Name", value="llama3")
    iterations = st.sidebar.number_input("Number of Iterations", value=10, min_value=1)

    prompts = [
        st.text_area("Prompt 1", value='''tell me something cool, 
but please don't just wank on about 
quantum or immortal jellyfish again'''),
        st.text_area("Prompt 2", value="Enter your second prompt here")
    ]

    if st.button('Generate Responses'):
        all_responses = generate_responses(model_name, prompts, iterations)
        for i, responses in enumerate(all_responses):
            st.subheader(f"Responses for Prompt {i+1}")
            for j, response in enumerate(responses):
                st.write(f"Response {j+1}: {response}")

if __name__ == "__main__":
    main()