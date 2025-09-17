from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = "Paste your openai api key here"

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=20, api_key = OPENAI_API_KEY)

result = embedding.embed_query("baramati is the big city")

print(str(result))
print(len(result))