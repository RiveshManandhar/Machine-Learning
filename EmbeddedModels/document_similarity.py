from langchain_litellm import LiteLLMEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise  import cosine_similarity
import numpy as np
import os

load_dotenv()

api_key = os.getenv("LITELLM__VIRTUAL_KEY")
base_url = os.getenv("LITELLM__BASEURL")

#   what dimension output do you want for the output vector, small dimension will lower the cost
#   For this model the max dimension is 1536 and for large model it can be 3072
embedding=LiteLLMEmbeddings(
                    model='openai/text-embedding-3-small'
                    ,dimensions=300
                    ,api_key=api_key
                    ,api_base=base_url
                    )

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query="Tell me about Virat Kohli"

doc_embedding=embedding.embed_documents(documents)

query_embedding=embedding.embed_documents(query)

#both the arguments must be a 2d list
scores=cosine_similarity(query_embedding,doc_embedding)[0]

list_enum_score=list(enumerate(scores))
sorted_score=sorted(list_enum_score,key=lambda x:x[1])

index,score=sorted_score[-1]

print(documents[index])
print("similarity score is: %s in index: %s" % (score, index))
