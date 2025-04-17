from langchain_openai import ChatOpenAI
import os

# Manually set the API key
os.environ["OPENAI_API_KEY"] = "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"  # Replace with your actual API key


# Pass the API key explicitly while initializing ChatOpenAI
model = ChatOpenAI(model='gpt-4',openai_api_key=os.environ["OPENAI_API_KEY"])

# Invoke the model
result = model.invoke("write a 5-line poem on cricket")

print(result.content)
