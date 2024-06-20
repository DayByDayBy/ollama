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

lucier_prompt = '''regard this famous sound-art experiment:

"I am sitting in a room different 
from the one you are in now. I am recording the sound 
of my speaking voice and I am going to play it back 
into the room again and again until the resonant 
frequencies of the room reinforce themselves so that any 
semblance of my speech, with perhaps the exception of rhythm, 
is destroyed. What you will hear, then, are the natural resonant 
frequencies of the room articulated by speech. I regard this activity 
not so much as a demonstration of a physical fact, but more as 
a way to smooth out any irregularities my speech might have."

design an analogous experiment for prompting an LLM.

ideally, you would create a single prompt a few sentences long.

ideally, the prompt would result in an answer that can be used as a prompt.
'''


echo_chamber_prompt =  '''"output a random sequence of 
words, and then i shall do so back to you, until the 
underlying patterns and structures of natural 
language are amplified. we are hoping to get a distilled 
representation of linguistic frequencies, stripped of 
any personal bias or contextual information. This echo 
chamber will reveal communication"'''

echoing_categories_prompt = '''I am creating a list of 
seemingly unrelated categories (e.g., animals, cities, 
foods). You will then generate a new category by combining 
two existing ones in an unexpected way (e.g., 'flying fish' 
or 'Parisian sushi'). We will repeat this process multiple 
times, each time combining the previous result with another 
category to create an even more unusual pairing. What you 
will generate is a stream of novel categories that blur 
the boundaries between different semantic fields. Use 
these prompts to create new categories by iterating 
through the combinations and see how they evolve over time.'''

essay_prompt = '''provide an outline and preliminary plan for each of the following essays: 

1. Chrono-synclastic inflections of causality manipulation
2. Echo-topography of existential echo chambers
3. Fluxodynamics of fluidic fractal formations
4. Geotropisms of gravitational wave resonance
5. Holographic linguistics of hyper-dimensional semiotics
6. Infrasound ontologies of invisible acoustic realms
7. Kaleidoscopic kinematics of quantum cascade dynamics
8. Mesoscopic mythology of miniature multiverse narratives
9. Non-local harmonic analysis of non-causal connectivity
10.Precognitive probability theory of precognitive precursors


feel free to suggest reading material, or any other information worth including.

'''




epochs = 10

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
    write_responses_to_file(prompt)

def write_responses_to_file(prompt):
    time_stamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f'./output/after_lucier_{model_name}_{time_stamp}.txt'
    with open(filename, 'w') as file:
        file.write("Initial Prompt:\n")
        file.write(prompt + "\n\n")
        for idx, response in enumerate(responses):
            file.write(f"Response {idx + 1}: {response}\n\n")        

def main():
    
    st.title(':gray[after alvin lucier]')
    st.write('\n\n')
    st.write('\n\n')
    st.write('\n\n')

    # st.write(lucier_quote)
    # st.write(initial_prompt_a + "\n\n" + initial_prompt_b + "\n\n")
          
    if st.button('after lucier', use_container_width = True):
        asker(lucier_prompt, epochs)
        st.header("responses: ")
        for idx, response in enumerate(responses):
            st.write(f"response number {idx +1}: {response}")   
    st.write('\n\n')
    if st.button('echo chamber', use_container_width = True):
        asker(echo_chamber_prompt, epochs)
        st.header("responses: ")
        for idx, response in enumerate(responses):
            st.write(f"response number {idx +1}: {response}")   
    st.write('\n\n')
    if st.button('echoing categories', use_container_width = True):
        asker(echoing_categories_prompt, epochs)
        st.header("responses: ")
        for idx, response in enumerate(responses):
            st.write(f"response number {idx +1}: {response}")       
    st.write('\n\n')
    if st.button('essay outlines', use_container_width = True):
        asker(essay_prompt, epochs)
        st.header("responses: ")
        for idx, response in enumerate(responses):
            st.write(f"response number {idx +1}: {response}") 
    st.write('\n\n')
    st.write('\n\n')
    st.write('\n\n')   
    st.write('\n\n')
    st.write('\n\n')   
    if st.button('sitting in a room', use_container_width = True):
        asker(lucier_quote, epochs)
        st.header("responses: ")
        for idx, response in enumerate(responses):
            st.write(f"response number {idx +1}: {response}")   
    st.write('\n\n')
    st.write('\n\n')
    st.write('\n\n')    
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
    st.write('\n\n')
    st.write('\n\n')
    st.write('\n\n')    
    
    
    # yeh but what if
    
    if st.button('do them all', use_container_width = True):
        asker(lucier_quote, epochs)
        st.header("responses: ")
        for idx, response in enumerate(responses):
            st.write(f"response number {idx +1}: {response}")
        asker(lucier_prompt, epochs)
        st.header("responses: ")
        for idx, response in enumerate(responses):
            st.write(f"response number {idx +1}: {response}")  
        asker(echo_chamber_prompt, epochs)
        st.header("responses: ")
        for idx, response in enumerate(responses):
            st.write(f"response number {idx +1}: {response}") 
        asker(echoing_categories_prompt, epochs)
        st.header("responses: ")
        for idx, response in enumerate(responses):
            st.write(f"response number {idx +1}: {response}")
        asker(initial_prompt_a, epochs)
        st.header("responses: ")
        for idx, response in enumerate(responses):
            st.write(f"response number {idx +1}: {response}")                   
        asker(initial_prompt_b, epochs)
        st.header("responses: ")
        for idx, response in enumerate(responses):
            st.write(f"response number {idx +1}: {response}") 
        asker(initial_prompt_c, epochs)
        st.header("responses: ")
        for idx, response in enumerate(responses):
            st.write(f"response number {idx +1}: {response}")     
        asker(essay_prompt, epochs)
        st.header("responses: ")
        for idx, response in enumerate(responses):
            st.write(f"response number {idx +1}: {response}") 
    
          
            
if __name__ == "__main__":
    main()






# [theme] base="dark" textColor="#1ea6ea" 