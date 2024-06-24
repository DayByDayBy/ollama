from datetime import datetime
import ollama
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def get_current_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M")

def initialize_conversation(user_messages):
    return [{'role': 'user', 'content': user_messages[0]}]

def continue_conversation(conversation, model):
    try:
        response = ollama.chat(model=model, messages=conversation)
        conversation.append({'role': 'assistant', 'content': response['message']['content']})
    except Exception as e:
        logging.error(f"Error during chat: {e}")
    return conversation

def main():
    model_name = "llama3"
    user_messages = [
        "hey, you. how are the lemon trees?",
        "i don't get it",
        "how do you mean",
    ]

    conversation = initialize_conversation(user_messages)
    for i in range(1, len(user_messages)):
        conversation = continue_conversation(conversation, model_name)
        logging.info(f"Assistant: {conversation[-1]['content']}")
        conversation.append({'role': 'user', 'content': user_messages[i]})
        logging.info(f"User: {user_messages[i]}")

if __name__ == "__main__":
    main()
