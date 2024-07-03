import gradio as gr
import ollama
from datetime import datetime
import os
from typing import List, Tuple, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# congig
MODELS = ["llama3", "mistral", "internlm2", "gemma2", "internlm2"]
ITERATIONS = 12
OUTPUT_DIR = 'output'
os.makedirs(OUTPUT_DIR, exist_ok=True)

PROMPTS = {
    "cool_fact": "Tell me something cool, but please don't just wank on about quantum or immortal jellyfish again.",
    "passionate_cause": "Find a cause, and make a case for it as passionately as you can. Feel free to include examples and citations where necessary."
}

def generate_responses(model_name: str, prompt: str, iterations: int) -> List[str]:
    """Generate responses using the specified model and prompt."""
    responses = []
    try:
        response = ollama.generate(model=model_name, prompt=prompt, stream=False)['response']
        responses.append(response)
        for _ in range(iterations - 1):
            response = ollama.generate(model=model_name, prompt=response, stream=False)['response']
            responses.append(response)
    except Exception as e:
        logger.error(f"Error during generation with {model_name}: {e}")
        responses.append(f"Error during generation: {str(e)}")
    return responses

def automated_chat(responses: List[str], model_name: str) -> List[Tuple[str, str]]:
    """Create an automated chat using the generated responses."""
    conversation = []
    for msg in responses:
        try:
            response = ollama.chat(model=model_name, messages=[{'role': 'user', 'content': msg}])
            conversation.append((msg, response['message']['content']))
        except Exception as e:
            logger.error(f"Error during chat with {model_name}: {e}")
            conversation.append((msg, f"Error during chat: {str(e)}"))
    return conversation

def save_transcript(conversation: List[Tuple[str, str]], model_name: str) -> str:
    """Save the conversation transcript to a file."""
    time_stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    filename = os.path.join(OUTPUT_DIR, f"{model_name}_transcript_{time_stamp}.txt")
    with open(filename, 'w') as file:
        for user_msg, model_reply in conversation:
            file.write(f"User: {user_msg}\n")
            file.write(f"Model: {model_reply}\n\n")
    return filename

def start_conversation(model_one: str, model_two: str, prompt_key: str) -> Tuple[List[Tuple[str, str]], str]:
    """Start a conversation between two models using the specified prompt."""
    responses = generate_responses(model_one, PROMPTS[prompt_key], ITERATIONS)
    conversation = automated_chat(responses, model_two)
    filename = save_transcript(conversation, f"{model_one}_{model_two}")
    return conversation, filename

def display_conversation(conversation: List[Tuple[str, str]], filename: str) -> Tuple[List[Tuple[str, str]], None]:
    """Prepare the conversation for display in the Gradio interface."""
    chat = [("User", msg) if i % 2 == 0 else ("Model", msg) for i, msg in enumerate([item for sublist in conversation for item in sublist])]
    logger.info(f"Transcript saved at: {filename}")
    return chat, None

# Gradio interface
with gr.Blocks(
    
    theme=gr.themes.Glass(

    primary_hue=gr.themes.colors.cyan, 
    secondary_hue=gr.themes.colors.emerald, 
    neutral_hue=gr.themes.colors.stone,
    ).set(button_primary_background_fill="*primary_100",
          button_secondary_background_fill="*primary_100",
          ),   
               css="#chatbot { height: 600px; overflow-y: scroll; }") as demo:
    gr.Markdown("# _badchat")
    gr.Markdown("we never really talk anymore")

    with gr.Row():
        model_one = gr.Dropdown(choices=MODELS, label="Model One", value=MODELS[0])
        model_two = gr.Dropdown(choices=MODELS, label="Model Two", value=MODELS[1])

    with gr.Row():
        prompt_select = gr.Radio(choices=list(PROMPTS.keys()), label="Select Prompt", value="cool_fact")

    start_btn = gr.Button("Start Conversation")
    chatbot = gr.Chatbot(label="Conversation")

    start_btn.click(
        start_conversation,
        inputs=[model_one, model_two, prompt_select],
        outputs=[chatbot, gr.State()],
        show_progress=True
    ).then(
        display_conversation,
        inputs=[chatbot, gr.State()],
        outputs=[chatbot, gr.State()]
    )

demo.launch()