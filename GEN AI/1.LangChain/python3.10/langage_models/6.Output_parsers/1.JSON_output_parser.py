from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()

model = ChatOpenAI()

parser = JsonOutputParser()

template = PromptTemplate(
    template = "Give me a 5 facts about {topic} \n {format_instruction}",
    input_variables = ['topic'],
    partial_variables = {'format_instruction': parser.get_format_instructions()}

)

# prompt = template.format()

chain = template | model | parser

result = chain.invoke({'topic':'elephant'})

print(result)

# print Format
print(parser.get_format_instructions())

# you cannot enforce schema enforce in json output parser so we should go for structured output parser
