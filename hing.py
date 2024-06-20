import streamlit as st
import ollama
import pandas as pd
import os

model_name = 'llam3'
data_loc = '/output'

def load_data(file_path):
    if file_path.endswith('.txt'):
        with open(file_path, 'r') as file:
            return file.read()
    else:
        raise ValueError("Unsupported file format")
def retrieve_information(query, data):
    results = []
    for item in data:
        if query.lower() in item.lower():
            results.append(item)
    return results

def generate_response(results, query):
    response = ollama.generate(prompt = results + query, model = model_name)
    return response
data_files = [f for f in os.listdir('data') if f.endswith(('.csv', '.txt'))]
data = [load_data(os.path.join('data', file)) for file in data_files]

st.title("RAGOllama")

query = st.text_input("Enter your query:")

if query:
    retrieved_data = retrieve_information(query, data)
    if retrieved_data:
        st.write("Retrieved Information:")
        for item in retrieved_data:
            st.write(item)
        
        response = generate_response(retrieved_data, query)
        st.write("Generated Response:")
        st.write(response)
    else:
        st.write("No relevant information found.")
