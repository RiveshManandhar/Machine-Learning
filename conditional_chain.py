from langchain_litellm import ChatLiteLLM
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
# This is new to run parallel chains
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from pydantic import BaseModel,Field
from typing import Annotated,Literal

load_dotenv()

api_key = os.getenv("LITELLM__VIRTUAL_KEY")
base_url = os.getenv("LITELLM__BASEURL")

class Feedback(BaseModel):
    sentiment :Annotated[Literal['Positive','Negative'],Field(description='Return sentiment of the review eithr negative or positive')]

model1=ChatLiteLLM(
                model='gpt-4'
                ,api_key=api_key
                ,api_base=base_url
                ,temperature=0.3
                # ,max_completion_tokens= 100
                )


parser1=PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(template='Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}'
                      ,input_variables=['feedback']
                      ,validate_template=True
                      ,partial_variables={'format_instruction':parser1.get_format_instructions()}
                      )


parser2=StrOutputParser()

classifier_chain=prompt1 | model1 | parser1


prompt2=PromptTemplate(template='Write appropriate message to this positve feedback \n {feedback}'
                       ,input_variables=['feedback']
                      ,validate_template=True
                      )

prompt3=PromptTemplate(template='Write appropriate message to this negative feedback \n {feedback}'
                       ,input_variables=['feedback']
                      ,validate_template=True
                      )


# result=classifier_chain.invoke({'feedback':'This is a great smart phone.'})
# In runnable branch we send multiple tupils in each tupil we pass condition and the chain and last default
branch_chain=RunnableBranch(
    (lambda x:x.sentiment=='Positive', prompt2 | model1 | parser2)
    ,(lambda x:x.sentiment=='Negative', prompt3 | model1 | parser2)
    # This is to convert lambda function into runnable
    ,RunnableLambda(lambda x : "Could not find sentiment")
)

final_chain= classifier_chain | branch_chain

result=final_chain.invoke({'feedback':'This is a terrible smart phone.'})

print(result)

final_chain.get_graph().print_ascii()