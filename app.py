import ollama


response = ollama.chat(model='gemma', messages=[
  {
    'role': 'user',
    'content': 'if we do, what shall we want?',
  },
])
print(response['message']['content'])
