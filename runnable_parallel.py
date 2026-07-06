from langchain_litellm import ChatLiteLLM
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel

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

template1=PromptTemplate(template="Generate a tweet about {topic}"
                        ,input_variables=['topic']
                        ,validate_template=True
                        )


template2=PromptTemplate(template="Generate a LinkedIn post about {topic}"
                        ,input_variables=['topic']
                        ,validate_template=True
                        )


parser=StrOutputParser()

parallel_chain =RunnableParallel({
    'tweet': RunnableSequence(template1,llm,parser)
    ,'linkedin':RunnableSequence(template2,llm,parser)

}
)

result=parallel_chain.invoke({'topic':'AI'})

print(result)