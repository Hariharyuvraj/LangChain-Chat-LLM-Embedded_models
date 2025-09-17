from langchain_openai import ChatOpenAI
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

OPENAI_API_KEY = "Paste your openai api key here"

#print(OPENAI_API_KEY)

load_dotenv()

model = ChatOpenAI(model="gpt-4",max_completion_tokens=50,temperature=0.9,

    api_key=OPENAI_API_KEY)

result = model.invoke("write 4 line poem for kids?")

print(result.content)

# "max_completion_tokens" this function is used for restrict the o/p token/words,(if you are using paid services then)  