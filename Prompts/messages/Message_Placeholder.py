"""
"MessagePlaceholder is used in LangChain to insert dynamic chat history or messages into a prompt template at runtime.
It doesn't store or retrieve messages itself, but acts as a slot to plug in past conversations — so the LLM has full context during a new interaction."

It's like a blank space in the prompt where I can later inject past chats or message history. That way, the model sees previous conversations, even though I didn't hardcode them.
"""

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder 
from langchain_core.messages import HumanMessage , AIMessage

# chat template
chat_templates =ChatPromptTemplate([
    ('system','you are a helpful customer agents'),
    MessagesPlaceholder(variable_name = 'chat_history'),
    ('human','{querry}')
])

# load chat history

chat_history=[]

with open(r'C:\Users\alisa\OneDrive\Desktop\LangChain\Prompts\messages\chat_history.txt', 'r') as f:
    for line in f:
        line = line.strip() # ised to cut space {starting , ending}
        if line.startswith("HumanMessage"):
            content = line[len('HumanMessage(content="'):-2]
            chat_history.append(HumanMessage(content=content))
        elif line.startswith("AIMessage"):
            content = line[len('AIMessage(content="'):-2]
            chat_history.append(AIMessage(content=content))

print(chat_history)

# create chat prompts
prompt = chat_templates.invoke({'chat_history': chat_history, 'querry':'my refund status'})

print(prompt)