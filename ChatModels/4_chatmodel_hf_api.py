from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

HUGGINGFACEHUB_ACCESS_TOKEN = "Paste your HUGGINGFACEHUB_ACCESS_TOKEN here"

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
HUGGINGFACEHUB_ACCESS_TOKEN = HUGGINGFACEHUB_ACCESS_TOKEN

result = model.invoke("what is the capital of india?")

print(result.content)


# by using this code we can interact with hugging face model.
# this model is rest on hugging face platform and we can access this with help of 'API_KEY'.