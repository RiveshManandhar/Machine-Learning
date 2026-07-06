from langchain_litellm import ChatLiteLLM
from dotenv import load_dotenv
import os

load_dotenv()


api_key = os.getenv("LITELLM__VIRTUAL_KEY")
base_url = os.getenv("LITELLM__BASEURL")

# we are passing  this to override it calling https://api.openai.com/v1 url.
# api_base tells your code to use your company's LiteLLM gateway instead of connecting directly to OpenAI.

llm=ChatLiteLLM(
                model='gpt-4'
                ,api_key=api_key
                ,api_base=base_url,  
                )

# we are sending a string as input 
response=llm.invoke('what is the capital of Nepal?')

# we get AIMessag object as output
print(type(response))
print(response)
print(response.content)