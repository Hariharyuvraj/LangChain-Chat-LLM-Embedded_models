from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = "Paste your openai api key here"

api_key=OPENAI_API_KEY

model = ChatOpenAI(model="gpt-4-turbo", api_key=OPENAI_API_KEY)

print("Hello my name is Chitti,how can i help you?")
print('To end the conversation please type "exit"')
while True:
    user_input = input('You:')
    if user_input == 'exit':
        print("ok Good By,Take Care")
        break
    result = model.invoke(user_input)
    print('Chitti: ',result.content)