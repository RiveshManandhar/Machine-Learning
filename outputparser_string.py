from langchain_litellm import ChatLiteLLM
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional, Literal
import os
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate

load_dotenv()

api_key = os.getenv("LITELLM__VIRTUAL_KEY")
base_url = os.getenv("LITELLM__BASEURL")

llm=ChatLiteLLM(
                model='gpt-4'
                ,api_key=api_key
                ,api_base=base_url
                ,temperature=0.3
                # ,max_completion_tokens= 100
                )

template1=PromptTemplate(
    template="""Write a detailed report on {topic}""",
    validate_template=True,
    input_variables=['topic']
)

template2=PromptTemplate(
    template="""Write a 5 line summary on the following text. /n {text}""",
    validate_template=True,
    input_variables=['text']
)


prompt1=template1.invoke({'topic':'Black Hole'})
response=llm.invoke(prompt1)

prompt2= template2.invoke({'text':response.content})
reposne2=llm.invoke(prompt2)

print(reposne2.content)