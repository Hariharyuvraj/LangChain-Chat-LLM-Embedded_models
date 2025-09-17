from langchain_openai import OpenAI
from dotenv import load_dotenv

OPENAI_API_KEY = "Paste your openai api key here"

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct',temperature=0.7, max_tokens=50,

    api_key=OPENAI_API_KEY)

result = llm.invoke("What you thik about the donald trump's recent tarrif decision against india?")

print(result)