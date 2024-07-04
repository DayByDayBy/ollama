# bad_chat


## an iterative LLM-botherer


- phase one: ollama.generate() - prompt=>response, response as prompt, prompt=>response, response as prompt, etc
- phase two: ollama.chat() - user: phase_one_resonse[0] => model_response, user: phase_one_resonse[1] => model_response, etc



#### key function: 

- def start_conversation:
    this function initiates a dialogue between two AI models. It uses a predefined prompt, runs for a set number of iterations, and manages the back-and-forth between the models. also saves the transcript and returns both the conversation and the filename
- def display_conversation:
    this function reformats the conversation for display in the gradio interface. it structures the chat into a user/model format and logs the transcript's location

these functions are handling the AI interaction and output preparation. start_conversation generates the content, while display_conversation formats it for presentation