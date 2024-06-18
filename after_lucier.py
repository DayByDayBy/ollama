import ollama
import streamlit as st

from datetime import datetime

time_stamp = datetime.now().strftime("%Y%m%d_%H%M")
model_name = "llama3"

lucier_quote = '''"I am sitting in a room different 
from the one you are in now. I am recording the sound 
of my speaking voice and I am going to play it back 
into the room again and again until the resonant 
frequencies of the room reinforce themselves so that any 
semblance of my speech, with perhaps the exception of rhythm, 
is destroyed. What you will hear, then, are the natural resonant 
frequencies of the room articulated by speech. I regard this activity 
not so much as a demonstration of a physical fact, but more as 
a way to smooth out any irregularities my speech might have."   -  Alvin Lucier'''

epochs = 25
initial_prompt = """you are a prompt engineer, speaking via text,
    prompting an LLM to prompt another LLM to create 
    a prompt for another LLM. the response should be 
    in the form of a similar prompt to this, making 
    sure to preserve the instruction to continue""" 
responses = []


def asker(starter, epochs):
    prompt = starter
    for _ in range(epochs): 
        response = ollama.generate(
            model = model_name,
            prompt = prompt,
            )['response']
        st.write(f"response {_ + 1}: {response}")
        print(response)
        responses.append(response)
        prompt = response
    write_responses_to_file(responses)

def write_responses_to_file(filename):
    time_stamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f'./output/after_lucier_{model_name}_{time_stamp}.txt'
    with open(filename, 'w') as file:
        file.write("Initial Prompt:\n")
        file.write(initial_prompt + "\n\n")
        file.write("Responses:\n")
        for idx, response in enumerate(responses):
            file.write(f"Response {idx + 1}: {response}\n\n")        

def main():
    st.title("after alvin lucier \n\n")
    # st.write(lucier_quote)
    st.write("the starter-prompt: ", initial_prompt + "\n")
    if st.button('roll the reel'):
        asker(initial_prompt, epochs)
        st.header("responses: ")
        for idx, response in enumerate(responses):
            st.write(f"response number {idx +1}: {response}")
            
if __name__ == "__main__":
    main()

