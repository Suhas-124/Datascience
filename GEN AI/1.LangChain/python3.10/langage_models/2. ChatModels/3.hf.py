import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API token from environment variables
hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

if not hf_token:
    raise ValueError("Hugging Face API token is missing. Please set it in the .env file.")

# Initialize Hugging Face endpoint with API key
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceTB/SmolLM2-1.7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=hf_token  # Add this parameter
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("what is capital of karnataka")
print(result.content)
