from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template = "write a summary of the following document - \n {text}",
    input_variables = ['text']
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt')

docs = loader.load()

print(docs)

print(type(docs))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

result = chain.invoke({'text':docs[0].page_content})

print(result)