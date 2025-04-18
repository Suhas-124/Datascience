from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema


load_dotenv()

model = ChatOpenAI()

schema = [
    ResponseSchema(name='fact_1',description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2',description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3',description='Fact 3 about the topic'),

]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'Give me a 3 fracts about {topic} \n {format_instruction}',
    input_variable = ['topic'],
    partial_variables = {'format_instruction':parser.get_format_instructions()}
    
)

chain = template | model | parser

result = chain.invoke({'topic':'lions'})

print(result)


# cannot do data validation in structured output parser so we should go for pydantic output parser
