from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_litellm import ChatLiteLLM
from dotenv import load_dotenv
import os

load_dotenv

api_key = os.getenv("LITELLM__VIRTUAL_KEY")
base_url = os.getenv("LITELLM__BASEURL")

llm=ChatLiteLLM(
                model='gpt-4'
                ,api_key=api_key
                ,api_base=base_url
                ,temperature=0.3
                # ,max_completion_tokens= 100
                )

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = llm.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)