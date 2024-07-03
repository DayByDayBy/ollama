import gradio as gr
import ollama
from datetime import datetime
import os

iterations = 10
model_one_name = "llama3"
model_two_name = "mistral"
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

prompt_one = '''tell me something cool, but please don't just wank on about quantum or immortal jellyfish again'''
prompt_two = '''find a cause, and, make a case for it, as passionately as you can. feel free to include examples and citations where necessary'''

def generate_responses(model_name, prompt, iterations):
    responses = []
    try:
        response = ollama.generate(model=model_name, prompt=prompt, stream=False)['response']
        responses.append(response)
        for _ in range(iterations - 1): 
            response = ollama.generate(model=model_name, prompt=response, stream=False)['response']
            responses.append(response)
    except Exception as e:
        responses.append(f"Error during generation: {e}")
    return responses

def automated_chat(responses, model_name):
    conversation = []
    for msg in responses:
        try:
            response = ollama.chat(model=model_name, messages=[{'role': 'user', 'content': msg}])
            conversation.append((msg, response['message']['content']))
        except Exception as e:
            conversation.append((msg, f"Error during chat: {e}"))
    return conversation

def save_transcript(conversation, model_name):
    time_stamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = os.path.join(output_dir, f"{model_name}_transcript_{time_stamp}.txt")
    with open(filename, 'w') as file:
        for user_msg, model_reply in conversation:
            file.write(f"User: {user_msg}\n")
            file.write(f"Model: {model_reply}\n\n")
    return filename

def conversation_one():
    responses = generate_responses(model_one_name, prompt_one, iterations)
    conversation = automated_chat(responses, model_two_name)
    filename = save_transcript(conversation, model_one_name)
    return conversation, filename

def conversation_two():
    responses = generate_responses(model_two_name, prompt_two, iterations)
    conversation = automated_chat(responses, model_one_name)
    filename = save_transcript(conversation, model_two_name)
    return conversation, filename

def display_conversation(conversation, filename):
    chat = []
    for user_msg, model_reply in conversation:
        chat.append(("User", user_msg))
        chat.append(("Model", model_reply))
    return chat, f"Transcript saved at: {filename}"

with gr.Blocks() as demo:
    gr.Markdown("# _badchat")
    gr.Markdown("we never really talk anymore")

    with gr.Row():
        with gr.Column():
            gr.Markdown(f"**Prompt One:**\n```\n{prompt_one}\n```")
            btn_one = gr.Button("roll convo")
            chat_one = gr.Chatbot(label="Conversation One")
            btn_one.click(conversation_one, outputs=[chat_one, gr.Textbox()], show_progress=True).then(display_conversation, inputs=[chat_one, gr.Textbox()], outputs=[chat_one, gr.Textbox()])

        # with gr.Column():
        #     gr.Markdown(f"**Prompt Two:**\n```\n{prompt_two}\n```")
        #     btn_two = gr.Button("Convo Two")
        #     chat_two = gr.Chatbot(label="Conversation Two")
        #     btn_two.click(conversation_two, outputs=[chat_two, gr.Textbox()], show_progress=True).then(display_conversation, inputs=[chat_two, gr.Textbox()], outputs=[chat_two, gr.Textbox()])

demo.launch(share=True)
