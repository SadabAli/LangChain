from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage 
from dotenv import load_dotenv 

load_dotenv() 

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash') 

chat_history=[
    SystemMessage(content='you are a helpful AI assistant')
]

while True:
    User_input = input('You: ') 
    chat_history.append(HumanMessage(content=User_input)) 
    if User_input == 'exit' :
        break 
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)

print(chat_history)
