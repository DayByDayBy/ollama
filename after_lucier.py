import ollama
import streamlit as st

    
prompt = '''as a prompt engineer, write an interesting prompt for an LLM. it should be framed as a request for an interesting prompt'''
epochs = 7

def asker(initial_prompt, epochs):
    prompt = initial_prompt
    
    for _, in range(epochs): 
        response = ollama.generate(prompt)
        st.write(f"response {_ + 1}: {response}")
        prompt = response
        
col1, col2, col3 = st.columns([3, 5, 5])
with col2:
    st.write(response['message']['content'])
    



# response1 = ollama.chat(
#     model='gemma', 
#     messages=[
#     {
#     'role': 'user',
#     'content': prompt2,
#     },
# ])

# response2 = ollama.chat(
#     model='llama2', 
#     messages=[
#     {
#     'role': 'user',
#     'content': prompt2,
#     },
# ])







# with st.chat_message("user"):
#     st.write(response1['message']['content'])
    
# with st.chat_message("admin"):
#     st.write(response2['message']['content'])
