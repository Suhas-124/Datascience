from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field,field_validator

load_dotenv()

model = ChatOpenAI()

class LionsFact(BaseModel):
    fact_1 : str = Field(description="Fact 1 about the topic\n")
    fact_2 : str = Field(description="Fact 2 about the topic\n")
    fact_3 : str = Field(description="Fact 3 about the topic\n")


parser = PydanticOutputParser(pydantic_object=LionsFact)


# Define the prompt template with format instructions

template = PromptTemplate(
    template = "Give me a 3 facts about {topic} \n {format_instructions}",
    input_variables = ["topic"],
    partial_variables = {"format_instructions":parser.get_format_instructions()}
)


# Create the chain (Prompt -> Model -> Parser)

chain = template | model | parser

result = chain.invoke({"topic":"Polar bear"})

print(result)

