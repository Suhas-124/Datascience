from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field,field_validator


load_dotenv()

model = ChatOpenAI()

class Person(BaseModel):
    name : str = Field(description='Name of the person')
    age : int = Field(gt=18,description = 'Age of the Person')
    city : str = Field(description = 'Name of the city the person belongs to')

    @field_validator("city")
    def city_must_start_with_d(cls, v):
        if not v.startswith("C"):
            raise ValueError("City name must start with 'C'")
        return v

parser = PydanticOutputParser(pydantic_object=Person)

# template = PromptTemplate(
#     template = 'Generate the name of the name,age and city of a frictional {place} person \n {format_instruction}',
#     input_variables = ['place'],
#     partial_variables = {'format_instruction':parser.get_format_instructions()}

# )

template = PromptTemplate(
    template="Generate the name, age, and a city (starting with 'C') of a fictional person from {place}. \n {format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

final_result = chain.invoke({'place':'India'})

print(final_result)