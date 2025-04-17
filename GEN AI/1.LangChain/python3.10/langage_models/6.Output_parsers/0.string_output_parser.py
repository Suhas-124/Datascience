from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()

# # Using Hugging face

# # Get the API token from environment variables
# hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

# # llm = HuggingFaceEndpoint(
# #     repo_id="google/gemma-2-2b-it",
# #     task="text-generation"
# # )

# llm = HuggingFaceEndpoint(
#     repo_id="mistralai/Mistral-7B-Instruct",
#     task="text-generation",
#     huggingfacehub_api_token=hf_token
# )

# model = ChatHuggingFace(llm=llm)

# # 1st prompt -> detailed report
# template1 = PromptTemplate(
#     template='Write a detailed report on {topic}',
#     input_variables=['topic']
# )

# # 2nd prompt -> summary
# template2 = PromptTemplate(
#     template='Write a 5 line summary on the following text. /n {text}',
#     input_variables=['text']
# )

# prompt1 = template1.invoke({'topic':'black hole'})

# result = model.invoke(prompt1)

# prompt2 = template2.invoke({'text':result.content})

# result1 = model.invoke(prompt2)

# print(result1.content)


# Using Chatopenai

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

# 1st prompt --> detailed report

template_1 = PromptTemplate(
    template = 'Write a detailed report on {topic}',
    inupt_variables = ['topic']
)

# 2nd prompt --> summary

template_2 = PromptTemplate(
    template = 'write a 5 point summary on the following text. \n {text}',
    input_variables = ['text']
)

parser = StrOutputParser()

chain = template_1 | model | parser | template_2 | model | parser


result = chain.invoke({'topic':'black hole'})

print(result)
