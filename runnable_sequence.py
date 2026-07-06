from langchain_litellm import ChatLiteLLM
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

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

template1=PromptTemplate(template="Write a joke about {topic}"
                        ,input_variables=['topic']
                        ,validate_template=True
                        )

parser=StrOutputParser()

template2=PromptTemplate(template="Explain the following joke {passage}"
                        ,input_variables=['passage']
                        ,validate_template=True
                        )

chain=RunnableSequence(template1,llm,parser,template2,llm,parser)

result=chain.invoke({'topic':'Apple'})

print(result)