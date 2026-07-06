from typing import TypedDict


class Person(TypedDict):

    name: str
    age : int

new_person=Person(name='Ram',age=30)

print(new_person)