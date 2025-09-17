from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = "Paste your openai api key here"

model = ChatOpenAI(api_key=OPENAI_API_KEY)

messages = [
    SystemMessage(content = "you are helpful assistant"),
    HumanMessage(content = "tell me about langchain")
    ]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)