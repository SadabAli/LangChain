"""
🧠 What it does:
Runs multiple runnables in order (one after another) like a pipeline.

💡 Use case:
Used when you want to do A ➝ B ➝ C step-by-step.
"""
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser 
from dotenv import load_dotenv 
from langchain.schema.runnable import RunnableSequence

load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt1= PromptTemplate(
    template = 'Write a joke {topic}',
    input_variable = ['topic']
)
prompt2= PromptTemplate(
    template= 'Explain the following {text}',
    input_variable=['text']
)

parser = StrOutputParser()

chain =RunnableSequence(prompt1,llm,parser,prompt2,llm,parser)

print(chain.invoke({'topic':'gender equality'}))