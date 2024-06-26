from datetime import datetime
import ollama
import json
import os
import logging

# logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def get_current_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M")

def load_config(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config

def initialize_conversation(user_messages):
    return [{'role': 'user', 'content': user_messages[0]}]

def continue_conversation(conversation, model):
    try:
        response = ollama.chat(model=model, messages=conversation)
        conversation.append({'role': 'assistant', 'content': response['message']['content']})
    except Exception as e:
        logging.error(f"Error during chat: {e}")
    return conversation

def print_conversation(conversation):
    for message in conversation:
        role = message['role'].capitalize()
        logging.info(f"{role}: {message['content']}")

def main():
    
    # config stuff
    config = load_config('../config.json')
    model_name = os.getenv("MODEL_NAME", config['model_name'])
    user_messages = config['user_messages']

    conversation = initialize_conversation(user_messages)

    for i in range(1, len(user_messages)):

        conversation.append({'role': 'user', 'content': user_messages[i-1]})
        logging.info(f"User: {user_messages[i-1]}")
        conversation = continue_conversation(conversation, model_name)
        logging.info(f"Assistant: {conversation[-1]['content']}")

    conversation.append({'role': 'user', 'content': user_messages[-1]})
    logging.info(f"User: {user_messages[-1]}")
    conversation = continue_conversation(conversation, model_name)
    logging.info(f"Assistant: {conversation[-1]['content']}")

if __name__ == "__main__":
    main()
