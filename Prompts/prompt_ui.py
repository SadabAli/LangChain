# all library
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_core.prompts import PromptTemplate,load_prompt

import os 
from dotenv import load_dotenv 
load_dotenv() 

import streamlit as st 
# google model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
# User Interface
st.header('Research tools')

# For dynamic prompts
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt(r'C:\Users\alisa\OneDrive\Desktop\LangChain\Prompts\template.json')


if st.button('Submit'):
    chain = template | model 
    results=chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(results.content)