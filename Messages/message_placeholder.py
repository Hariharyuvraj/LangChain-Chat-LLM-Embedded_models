from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# Your API key
OPENAI_API_KEY = "your_api_key_here"

# Initialize the chat model
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    api_key=OPENAI_API_KEY
)

# Conversation memory (keeps history in RAM)
memory = ConversationBufferMemory(return_messages=True)

# Create a conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# Example conversation
print(conversation.predict(input="Hi, who are you?"))
print(conversation.predict(input="What do you think about Indian corruption?"))
print(conversation.predict(input="Can you summarize what I just asked?"))
