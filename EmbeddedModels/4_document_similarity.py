from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

OPENAI_API_KEY = "Paste your openai api key here"

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=20, api_key = OPENAI_API_KEY)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "tell me about sachin"         

doc_embeddings = embedding.embed_documents(documents)
query_embeddings = embedding.embed_query(query)

# To findout the cosine similarity in between query_embedding and dcocument_embedding

score = cosine_similarity([query_embeddings], doc_embeddings)[0]

index, score = (sorted(list(enumerate(score)),key=lambda x:x[-1]))[-1]


print(query)                          # to print query of user
print(documents[index])               # to print the similar information  from documents
print("similarity score of query and document is:", score)     # to know the similarity score between them


