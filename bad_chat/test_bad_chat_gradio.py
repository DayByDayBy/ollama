import pytest
from bad_chat_gradio import generate_responses, automated_chat, save_transcript

def test_generate_responses():
    responses = generate_responses("llama3", "Test prompt", 2)
    assert len(responses) == 2
    assert all(isinstance(r, str) for r in responses)

def test_automated_chat():
    conversation = automated_chat(["Hello", "How are you?"], "mistral")
    assert len(conversation) == 2
    assert all(isinstance(msg, tuple) and len(msg) == 2 for msg in conversation)

def test_save_transcript(tmp_path):
    conversation = [("User", "Hello"), ("Model", "Hi there")]
    filename = save_transcript(conversation, "test_model", output_dir=tmp_path)
    assert tmp_path.joinpath(filename).exists()

