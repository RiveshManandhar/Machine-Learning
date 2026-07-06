from abc import ABC,abstractmethod
import random

class runnable(ABC):

    @abstractmethod
    def invoke(input_data):
        pass

class DemoLLM(runnable):

    def __init__(self):
        print('llM created')

    def invoke(self,prompt):

        response_list=[
          'Kathmandu is the capital of Nepal',
          'IPL is a cricket leauge',
          'AI stands for Artificial Intelligence'  
        ]

        return {'response':random.choice(response_list)}

    def predict(self,prompt):

        response_list=[
          'Kathmandu is the capital of Nepal',
          'IPL is a cricket leauge',
          'AI stands for Artificial Intelligence'  
        ]

        return {'response':'In Future this feature is going to be depricaated'}

class DemoPromptTemplate(runnable):
    def __init__(self,template,input_variables):
        self.template=template
        self.input_variables=input_variables
    
    def invoke(self,input_dict):
        return self.template.format(**input_dict)

    def format(self,input_dict):
        return self.template.format(**input_dict)

class DemoStrParser(runnable):
    def __init__(self):
        pass

    def invoke(self,input_dict):
        return input_dict['response']



#Now what i have done is 
# 1. made both runnable
# 2. added common function to both the classes

#The advantage is that we can now create long chains

class RunnableConnector(runnable):

    def __init__(self,runnable_list):
        self.runnable_list=runnable_list
    
    def invoke(self,input_data):

        for runnable in self.runnable_list:
            input_data=runnable.invoke(input_data)

        return input_data
    
template=DemoPromptTemplate(template='Write a {lenght} poem about {topic}'
                            ,input_variables=['topic','lenght'])

llm=DemoLLM()

parser=DemoStrParser()

chain=RunnableConnector([template,llm,parser])


result=chain.invoke({'topic':'USA','lenght':'short'})

print(result)

# ====================================== THIS CODE IS A DEMO TO CONNECT 2 OR MORE RUNNABLES =========================

template1=DemoPromptTemplate(template='Write a joke about {topic}'
                            ,input_variables=['topic'])

template2=DemoPromptTemplate(template='Explain the following joke {response}'
                            ,input_variables=['response'])

llm=DemoLLM()

parser=DemoStrParser()

chain1=RunnableConnector([template1,llm])

result1=chain1.invoke({'topic':'USA'})

print(result1)

chain2=RunnableConnector([template2,llm,parser])

final_chain=RunnableConnector([chain1,chain2])

result_final=final_chain.invoke({'topic':'USA'})

print(result_final)