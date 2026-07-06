from langchain_litellm import ChatLiteLLM
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional, Literal
import os
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

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


parser=JsonOutputParser()

template=PromptTemplate(
    template="""Give me the name ,age and city of a fictional person \n {format_instruction}""",
    validate_template=True,
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# prompt=template.format()

# result=llm.invoke(prompt)

# content=parser.parse(result.content)

# print(type(content))

# print(content)

# we can use chains instead of the above steps

chain = template | llm | parser

content=chain.invoke({}) # {} this is for empty input . This is mandatory

print(type(content))

print(content)
