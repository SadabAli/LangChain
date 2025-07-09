"""
HumanMessage: Represents the user’s message (like a question or prompt).
SystemMessage: Represents instructions or behavior settings for the LLM(let you are a ML ENG. with 10+ experiance).
AIMessage: Used to store the AI model’s response — helpful when you want to simulate a conversation.
"""




from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI  
from dotenv import load_dotenv 

load_dotenv() 

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash') 

messages=[
    SystemMessage(content='you are a helpful assistant'),
    HumanMessage(content='tell me about Sadab Ali')
]

results=model.invoke(messages)
messages.append(AIMessage(content=results.content))

print(results)