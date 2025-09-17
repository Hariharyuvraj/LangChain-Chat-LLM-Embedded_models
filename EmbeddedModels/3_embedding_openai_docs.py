from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = "Paste your openai api key here"

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=20, api_key = OPENAI_API_KEY)

documents = [
    "SQL stands for Structured Query Language"
    "It is aprogramming language used for managing andmanipulating relational databases"
    "A database is an organized collection of data storedand accessed electronically"
]

result = embedding.embed_documents(documents)
print(result)