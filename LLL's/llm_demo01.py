from langchain_openai import OpenAI
from dotenv import load_dotenv

# Define your API key directly here
OPENAI_API_KEY = "Paste your openai api key here"

# Initialize the model
llm =OpenAI(
    model="gpt-3.5-turbo-instruct",
    temperature=1.3,
    max_tokens=50,
    api_key=OPENAI_API_KEY
    )

# Send a simple query
response = llm.invoke("what you think about indian curruption?")
print(response)
