from langchain_litellm import ChatLiteLLM
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

api_key = os.getenv("LITELLM__VIRTUAL_KEY")
base_url = os.getenv("LITELLM__BASEURL")

prompt1=PromptTemplate(template='Generate a detailed report on {topic}'
                      ,input_variables=['topic']
                      ,validate_template=True)

prompt2=PromptTemplate(template='Generate a 5 pointer summary from followin text \n {text}'
                      ,input_variables=['text']
                      ,validate_template=True)
model=ChatLiteLLM(
                model='gpt-4'
                ,api_key=api_key
                ,api_base=base_url
                ,temperature=0.3
                # ,max_completion_tokens= 100
                )

parser=StrOutputParser()

chain= prompt1 | model | parser | prompt2 | model | parser

result=chain.invoke({'topic':'Unemployment in Nepal'})

print(result)

chain.get_graph().print_ascii()
