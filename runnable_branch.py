from langchain_litellm import ChatLiteLLM
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda,RunnableBranch

load_dotenv()

# This is a python function which we will convert to runnable
def word_count(text):
    return len(text.split())

api_key = os.getenv("LITELLM__VIRTUAL_KEY")
base_url = os.getenv("LITELLM__BASEURL")

llm=ChatLiteLLM(
                model='gpt-4'
                ,api_key=api_key
                ,api_base=base_url
                ,temperature=0.3
                # ,max_completion_tokens= 100
                )

template1=PromptTemplate(template="Write a detailed report on {topic}"
                        ,input_variables=['topic']
                        ,validate_template=True
                        )

template2=PromptTemplate(template="Summarize the following text \n {text}"
                        ,input_variables=['text']
                        ,validate_template=True
                        )

parser=StrOutputParser()

report_generation_chain=RunnableSequence(template1,llm,parser)

branch_chain=RunnableBranch(
    (lambda x:len(x.split())>300,RunnableSequence(template2,llm,parser))
    ,RunnablePassthrough()
)

final_chain=RunnableSequence(report_generation_chain,branch_chain)

result=final_chain.invoke({'topic':'Russia Vs Ukraine'})

print(result)