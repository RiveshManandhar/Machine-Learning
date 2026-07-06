from langchain_litellm import ChatLiteLLM
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional, Literal
import os
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

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


parser=StrOutputParser()

chain=template1 | llm | parser | template2 | llm | parser

result=chain.invoke({'topic':'Black Hole'})

print(result)