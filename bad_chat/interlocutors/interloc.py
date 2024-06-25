import ollama
from datetime import datetime


time_stamp = datetime.now().strftime("%Y%m%d_%H%M")
epochs = 10
model_name = "gemma"

convo_one = []
convo_two = []

def one_into_two():
    response = ollama.chat()
    
    convo_one.append(response)
    return convo_one
    
def two_into_one():
    convo_two.append()
    return convo_two

# resulting_convos = [
#     {
#     convo_one[idx], 
#     convo_one['response']
#     }
#                     ]










    # for _ in range(epochs):
    #     ollama.chat