from langchain_litellm import ChatLiteLLM
from dotenv import load_dotenv
import os

load_dotenv()


api_key = os.getenv("LITELLM__VIRTUAL_KEY")
base_url = os.getenv("LITELLM__BASEURL")

# we are passing  this to override it calling https://api.openai.com/v1 url.
# api_base tells your code to use your company's LiteLLM gateway instead of connecting directly to OpenAI.

# temperature is the paramenet that controls the randomness of the output (creativness) (0-0.3 predictable)

# 0-0.3-factual codes
# 0.5-0.7-general QA, explanation
# 0.9-1.2-jokesmstorytelling
# 1.5+ wild idea,brainstrome

# max_completion_tokens how many token/words(not exactly) in output
llm=ChatLiteLLM(
                model='gpt-4'
                ,api_key=api_key
                ,api_base=base_url
                ,temperature=0.3
                # ,max_completion_tokens= 100
                )

# we are sending a string as input 
response=llm.invoke('suggest me 5 Nepali male names.')

# we get AIMessag object as output
print(type(response))
print(response)
print(response.content)