from langchain_litellm import ChatLiteLLM
from dotenv import load_dotenv
import os
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from typing import List

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

class Author(BaseModel):
    name: str
    nationality: str


class Book(BaseModel):
    title: str
    year: int


class AuthorProfile(BaseModel):
    author: Author
    famous_books: List[Book]
    summary: str

parser=PydanticOutputParser(pydantic_object=AuthorProfile)

template=PromptTemplate(
    template='Generate information about the author {author_name}. \n {format_instructions} \n Rules: \n - Return ONLY valid JSON. \n - Include exactly 3 famous books. \n - The year field must be an integer. \n - The summary should be 2-3 sentences long.',
    input_variables=['author_name'],
    validate_template=True,
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

# prompt=template.invoke({'author_name':'J. K. Rowling'})

# result=llm.invoke(prompt)

# parsed=(parser.parse(result.content))

# final=parsed.model_dump()

# print(final)

chain= template | llm | parser 

final=chain.invoke({'author_name':'J. K. Rowling'})

final_dump=final.model_dump()

print(final_dump)