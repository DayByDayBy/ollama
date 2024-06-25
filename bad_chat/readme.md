# badChat

________________________________________________________________


another LLM botherer, this time PvP



________________________________________________________________


###### _(FYI: this readme is a plan as much as a description, as i only started thinking about this last night, and havent had a chance to code it all up)_

##   the basic idea

- prompt_one and prompt_two both take a starter prompt and use .generate() to create an iterative prompt chain (response becomes prompt, repeated based on iterations variable)
- prompt_one is set up to use llama3, prompt_two is set up to use gemma (variable to look for in most scripts in the repo is 'model_name').  this will almost certainly change, and may settle on other models/combinations

the results are then to be fed into an instance of .chat() as the user

this means that, in a largely unhelpful and fairly miselading sense, lamma3 and gemma will be conversing

- .generate() is being used for the initial genration and iteration. 

it takes longer, but it won't need to run 'live', and will not require retention of chat history between prompt=>repsonse cycles. 

- .chat() is used for the 'conversation' phase. 

it _will_ remember the context of the conversation, treating each message as part of a sequence of repplies betweeen interlocutors. this also means the LLM will be interpreting teh user messages as a responsive sequence in the context of the prior messages, even though the messages are actually pre-written and in no way repsonsive. 


### oh, yeah, also

i asked chatGPT to draft the above because why not, and bless, it had a wee go:

```badChat is a unique PvP (Player vs Player) LLM (Large Language Model) project that generates iterative prompt chains using different models, then makes them converse in a simulated chat. This project explores the interaction between LLMs in a dynamic and creative way.```

```badChat utilizes two different LLMs, initially set as `llama3` and `gemma`, to generate iterative prompt chains. Each prompt chain starts with a starter prompt and uses the `.generate()` method to create a sequence of responses. These responses are then fed into an instance of `.chat()` to simulate a conversation.```

not quite there... for one thing it's not player vs player, it's Prompt V Prompt, but of course LLMs prefer the well worn path, so it's defualting to the far more common phrase. 

i may give it more to write later, see how it copes once the project is further on, so it has more to work with 

---





## running it locally 
### requires:

```
ollama
streamlit
datetime
```

### Components
1. **Prompt Generation**
   - `prompt_one` uses `llama3` and `ollama.generate()`
   - `prompt_two` uses `gemma` and `ollama.generate()`

2. **conversation imulation**
   - The results from the prompt chains are fed into `.chat()` instances of the other chain's model

## installation

### requirements

- `ollama`
- `streamlit`
- `datetime`

You can install these dependencies using pip:

```bash
pip install ollama streamlit datetime
```

venv use is also recommended, but hey, i'm not your supervisor
