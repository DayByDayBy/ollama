# import unittest
# import os
# from unittest.mock import patch
# from bad_chat_gradio import generate_responses, automated_chat, save_transcript, start_conversation, display_conversation

# class TestYourModule(unittest.TestCase):

#     @patch('ollama.generate')
#     def test_generate_responses(self, mock_generate):
#         mock_generate.return_value = {'response': 'Test response'}
#         responses = generate_responses('test_model', 'test_prompt', 3)
#         self.assertEqual(len(responses), 3)
#         self.assertEqual(responses[0], 'Test response')

#     @patch('ollama.chat')
#     def test_automated_chat(self, mock_chat):
#         mock_chat.return_value = {'message': {'content': 'Test chat response'}}
#         responses = ['Test prompt 1', 'Test prompt 2']
#         conversation = automated_chat(responses, 'test_model')
#         self.assertEqual(len(conversation), 2)
#         self.assertEqual(conversation[0], ('Test prompt 1', 'Test chat response'))

#     def test_save_transcript(self):
#         conversation = [('User message', 'Model response')]
#         filename = save_transcript(conversation, 'test_model')
#         self.assertTrue(os.path.exists(filename))
#         os.remove(filename)

#     @patch('ollama.generate')
#     @patch('ollama.chat')
#     def test_start_conversation(self, mock_chat, mock_generate):
#         mock_generate.return_value = {'response': 'Test response'}
#         mock_chat.return_value = {'message': {'content': 'Test chat response'}}
#         conversation, filename = start_conversation('test_model_one', 'test_model_two', 'a fact', 3)
#         self.assertEqual(len(conversation), 4)  # 1 initial prompt + 3 responses
#         self.assertTrue(os.path.exists(filename))
#         os.remove(filename)

#     def test_display_conversation(self):
#         conversation = [('Initial Prompt', 'Test initial prompt'), ('Test prompt', 'Test response')]
#         chat, _ = display_conversation(conversation, 'test_filename')
#         self.assertEqual(len(chat), 3)
#         self.assertEqual(chat[0], ('System', 'Initial Prompt: Test initial prompt'))
#         self.assertEqual(chat[1], ('User', 'Test prompt'))
#         self.assertEqual(chat[2], ('Model', 'Test response'))

# if __name__ == '__main__':
#     unittest.main()
