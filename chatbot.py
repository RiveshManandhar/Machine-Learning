from langchain_litellm import ChatLiteLLM
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("LITELLM__VIRTUAL_KEY")
base_url = os.getenv("LITELLM__BASEURL")

model=ChatLiteLLM(
                model='gpt-4'
                ,api_key=api_key
                ,api_base=base_url
                ,temperature=0.3
                # ,max_completion_tokens= 100
                )


chat_history=[
    SystemMessage(content='You are a helpful AI assistant')
]

while True:
    user_input = input('You : ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(result.content))
    print("AI : ",result.content)

print(chat_history)

