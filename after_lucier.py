import ollama
import streamlit as st

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

epochs = 7
initial_prompt = "as a prompt engineer, write an interesting prompt for an LLM. it should be framed as a request for an interesting prompt"
responses = []


def asker(starter, epochs):
    for _ in range(epochs): 
        response = ollama.generate(
            model = "llama2",
            prompt = starter
            )  
        st.write(f"response {_ + 1}: {response}")
        responses.append(response)
        prompt = response['message']

def main():
    st.title("after alvin lucier \n\n")
    st.write(lucier_quote)
    st.write("the starter-prompt: ", initial_prompt + "\n")
    if st.button('roll the reel'):
        asker(initial_prompt, epochs)
        st.header("responses: ")
        for idx, response in enumerate(responses):
            st.write(f"response number {idx +1}: {response}")
            
if __name__ == "__main__":
    main()

