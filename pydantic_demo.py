from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str = 'Ram' #providing default values
    age: Optional[int]=None
    email : Optional[EmailStr]=None
    cgpa : float = Field(gt=0,lt=10,default=8,description='decimal value representing the cgpa of the student')


new_student={'name':'Ravi','age':32}
new_student1={'email':'Raqm@gmail.com'}
new_student3={'age':'31','email':'Raqm@gmail.com'}


s1=Student(**new_student)

print(s1.name)
print(s1.age)
print(type(s1))

s2=Student(**new_student1)

print(s2.name)
print(s2.age)
print(type(s2))

s3=Student(**new_student3)

print(s3.name)
print(s3.age)
print(s3.email)
print(s3.cgpa)
print(type(s3))

student_dict=s3.model_dump()
print(student_dict['email'])
