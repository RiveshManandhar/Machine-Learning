from langchain_litellm import ChatLiteLLM
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough

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

joke_gen_chain=RunnableSequence(template1,llm,parser)

explain_chain=RunnableSequence(template2,llm,parser)

passthorugh=RunnablePassthrough()

print(passthorugh.invoke(2))

new_chain=RunnableParallel({
    'joke':RunnablePassthrough()
    ,'explanation':explain_chain
}
)

chain=RunnableSequence(joke_gen_chain,new_chain)

result=chain.invoke({'topic':'Apple'})

print(result)