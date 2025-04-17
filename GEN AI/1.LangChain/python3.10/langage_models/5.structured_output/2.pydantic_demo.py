from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):

    name : str
    # name : str = 'ram' # set default

    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt=0,lt=10,default=5,description = "A decimal value representing the cgpa of the student")


new_student = {'name':'suhas','age': '32','email':'agb@gmail.com','cgpa':9}

# set default

student = Student(**new_student)

print(student)
print(type(student))
print(student.name) 
print(student.age)
print(type(student.age))
print(student.email)
print(student.cgpa)

# converion pydantic to dict,json

print(dict(student))
print(type(student))

student_json = student.model_dump_json()

print(student_json)