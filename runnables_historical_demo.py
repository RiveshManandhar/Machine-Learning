import random

class DemoLLM:

    def __init__(self):
        print('llM created')

    def predict(self,prompt):

        response_list=[
          'Kathmandu is the capital of Nepal',
          'IPL is a cricket leauge',
          'AI stands for Artificial Intelligence'  
        ]

        return {'response':random.choice(response_list)}

class DemoPromptTemplate:
    def __init__(self,template,input_variables):
        self.template=template
        self.input_variables=input_variables
        
    def format(self,input_dict):
        return self.template.format(**input_dict)

# llm=DemoLLM()

# response=llm.predict('what is a capital of nepal?')

# print(response)

# template=DemoPromptTemplate(template='Write a {lenght} poem about {topic}'
#                             ,input_variables=['topic','lenght'])

# prompt=template.format({'topic':'Nepal','lenght':'short'})

# response_final=llm.predict(prompt)

# print(response_final)

## Now lets say i am an AI engineer and i am given 2 componentes
## I need to create an app that used the prompt and the llm and gives me response

class demollmchain:
    def __init__(self,llm,prompt):
        self.llm=llm
        self.prompt=prompt

    def run(self,input_dict):
        final_prompt=self.prompt.format(input_dict)
        result=self.llm.predict(final_prompt)

        return result['response']
    

template=DemoPromptTemplate(template='Write a {lenght} poem about {topic}'
                            ,input_variables=['topic','lenght'])

llm=DemoLLM()

chain=demollmchain(llm,template)

result=chain.run({'topic':'USA','lenght':'short'})

print((result))