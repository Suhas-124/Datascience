# from langchain_community.document_loaders import CSVLoader

# loader = CSVLoader(file_path='Social_Network_Ads.csv')

# docs = loader.load()

# print(len(docs))
# print(docs[1])


from langchain_community.document_loaders import CSVLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import pandas as pd
from scipy.stats import ttest_ind

# Load environment variables
load_dotenv()

# Initialize OpenAI model
model = ChatOpenAI()

# Load CSV using LangChain
loader = CSVLoader(file_path="Social_Network_Ads.csv")
docs = loader.load()

# Convert docs to DataFrame
df = pd.DataFrame([doc.metadata for doc in docs])

# Create Prompt
prompt = PromptTemplate(
    template="Perform feature selection using t-test and find p-values for all features against the target variable 'Purchased'.\n\nData:\n{text} and give the output also",
    input_variables=["text"]
)

# Convert DataFrame to text for LLM processing
df_text = df.to_string()

# Initialize parser
parser = StrOutputParser()

# Create chain
chain = prompt | model | parser

# Invoke chain with the dataset
result = chain.invoke({"text": df_text})

# Print the result
print(result)

