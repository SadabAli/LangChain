from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
load_dotenv() 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import JsonOutputParser

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
parser = JsonOutputParser()

# 1st template 
template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'Hate'})

print(result)