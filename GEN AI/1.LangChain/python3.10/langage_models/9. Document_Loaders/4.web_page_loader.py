from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template = "Answer the following question \n {question} from the following text = \n {text}",
    input_variables = ['question','text']
)

parser = StrOutputParser()

url = "https://python.langchain.com/docs/integrations/document_loaders/"

loader = WebBaseLoader(url)

doc = loader.load()

chain = prompt | model | parser

result = chain.invoke({'question':'Name five document laoders in 2-3 lines summary','text':doc[0].page_content})


print(result)

