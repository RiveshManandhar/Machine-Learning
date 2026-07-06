from langchain_litellm import ChatLiteLLM
from dotenv import load_dotenv
import os
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

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

class Facts(BaseModel):
    fact_1: str = Field(description="Fact 1 about the topic")
    fact_2: str = Field(description="Fact 2 about the topic")
    fact_3: str = Field(description="Fact 3 about the topic")

parser=PydanticOutputParser(pydantic_object=Facts)

template=PromptTemplate(
    template='Give 3 facts about the {topic} \n {format_instruction}',
    input_variables=['topic'],
    validate_template=True,
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt=template.invoke({'topic':'Black Hole'})

result=llm.invoke(prompt)

parsed=(parser.parse(result.content))

final=parsed.model_dump()

print(final)