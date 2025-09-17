from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-3.5-sonnet-20241022')

result = model.invoke('what is the cappital of india?')

print(result)


# we can use this code to interact with the 'anthropic model'
# for interact with this you should have API_KEY fron anthropic.