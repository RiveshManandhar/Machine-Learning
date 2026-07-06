from langchain_litellm import ChatLiteLLM
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
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

prompt=PromptTemplate(
    template='Generate 5 intresting facts about {topic}'
    ,input_variables=['topic']
    ,validate_template=True
    )

parser=StrOutputParser()

chain=prompt | model | parser

result=chain.invoke({'topic':'Nepal'})

print(result)

# In order to visualize chains we can use the function chain.get_graph().print_ascii() pip install grandalf

chain.get_graph().print_ascii()