from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Define your OpenAI API Key directly
OPENAI_API_KEY = "Paste your openai api key here"

# Initialize the LLM (Chat Model)
llm = ChatOpenAI(
    model="gpt-4-turbo",
    temperature=0.7, max_completion_tokens=50,
    api_key=OPENAI_API_KEY
)

print(" Chatbot is ready, How can i help you. To end the conversation Type 'exit'\n")

# Chat loop
while True:
    user_input = input("You: ")
    if user_input == "exit":
        print("Chatbot: Goodbye,Take Care")
        break
    
    # Get response from LLM
    response = llm.invoke(user_input)
    print("Chatbot:", response.content)

