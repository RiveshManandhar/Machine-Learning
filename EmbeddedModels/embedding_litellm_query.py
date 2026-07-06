from langchain_litellm import LiteLLMEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("LITELLM__VIRTUAL_KEY")
base_url = os.getenv("LITELLM__BASEURL")

#   what dimension output do you want for the output vector, small dimension will lower the cost
#   For this model the max dimension is 1536 and for large model it can be 3072
embedding=LiteLLMEmbeddings(
                    model='openai/text-embedding-3-small'
                    ,dimensions=32
                    ,api_key=api_key
                    ,api_base=base_url
                    )

result= embedding.embed_query("Kathmandu is the capital of Nepal.")

print(result)