import ollama
import streamlit as st
from datetime import datetime

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.postimg.cc/4xgNnkfX/Untitled-design.png");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)





time_stamp = datetime.now().strftime("%Y%m%d_%H%M")
model_name = "llama3"

lucier_quote = '''I am sitting in a room different 
from the one you are in now. I am recording the sound 
of my speaking voice and I am going to play it back 
into the room again and again until the resonant 
frequencies of the room reinforce themselves so that any 
semblance of my speech, with perhaps the exception of rhythm, 
is destroyed. What you will hear, then, are the natural resonant 
frequencies of the room articulated by speech. I regard this activity 
not so much as a demonstration of a physical fact, but more as 
a way to smooth out any irregularities my speech might have.'''

epochs = 13

initial_prompt_a = """you are a prompt engineer, speaking via text,
    prompting an LLM to prompt another LLM to create 
    a prompt for another LLM. the response should be 
    in the form of a similar prompt to this, making 
    sure to preserve the instruction to continue"""
initial_prompt_b = """ask a question, 
    the answer to which will also be a question, 
    the answer to which will also be a question"""
initial_prompt_c = """'this sentence is false.' argue the affirmative for this motion, and then yield to your opponent, invting him to rebut."""
 
responses = []


def asker(starter, epochs):
    prompt = starter
    for _ in range(epochs): 
        response = ollama.generate(
            model = model_name,
            prompt = prompt,
            )['response']
        st.write(f"response {_ + 1}: {response}")
        print(_, response)
        responses.append(response)
        prompt = response
    write_responses_to_file(responses)

def write_responses_to_file(filename):
    time_stamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f'./output/after_lucier_{model_name}_{time_stamp}.txt'
    with open(filename, 'w') as file:
        file.write("Initial Prompt:\n")
        file.write(initial_prompt_a + "\n\n")
        for idx, response in enumerate(responses):
            file.write(f"Response {idx + 1}: {response}\n\n")        

def main():
    
    st.title(':gray[after alvin lucier]')
    st.write('\n\n')
    st.write('\n\n')
    st.write('\n\n')

    # st.write(lucier_quote)
    # st.write(initial_prompt_a + "\n\n" + initial_prompt_b + "\n\n")
    if st.button('prompting loop a', use_container_width = True):
        asker(initial_prompt_a, epochs)
        st.header("responses: ")
        for idx, response in enumerate(responses):
            st.write(f":gray[response number {idx +1}: {response}]")
    if st.button('prompting loop b', use_container_width = True):
        asker(initial_prompt_b, epochs)
        st.header("responses: ")
        for idx, response in enumerate(responses):
            st.write(f"response number {idx +1}: {response}")
    if st.button('prompting loop c', use_container_width = True):
        asker(initial_prompt_c, epochs)
        st.header("responses: ")
        for idx, response in enumerate(responses):
            st.write(f"response number {idx +1}: {response}")  
    if st.button('sitting in a room', use_container_width = True):
        asker(lucier_quote, epochs)
        st.header("responses: ")
        for idx, response in enumerate(responses):
            st.write(f"response number {idx +1}: {response}")            
            
if __name__ == "__main__":
    main()