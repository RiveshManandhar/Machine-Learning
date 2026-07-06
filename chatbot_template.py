from langchain_litellm import ChatLiteLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
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

# chat_template=ChatPromptTemplate.from_messages(
#                                                 [
#                                                     SystemMessage(content="You are a helpful {domain} expert"),
#                                                     HumanMessage(content="Explain in simple terms, what is {topic}")
#                                                 ]
#                                             )

# rather than creating prompts using from langchain_core.messages import SystemMessage,HumanMessage,AIMessage classes
# this is another way to create a prompt

chat_template=ChatPromptTemplate.from_messages(
                                                [
                                                    ("system","You are a helpful {domain} expert"),
                                                    ("human","Explain in simple terms, what is {topic}")
                                                ]
                                            )

chain = chat_template | llm
result = chain.invoke({
    'domain':'Cricket',
    'topic':'Dusra'
})

result=chain.invoke({'domain':'Cricket','topic':'Dusra'})

print(result.content)