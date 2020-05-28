from fastapi import FastAPI
from pydantic import BaseModel

from studentService import Student_Service



class Student(BaseModel):
    id: int
    name: str
    surname: str


app = FastAPI()

student_service = Student_Service()



@app.get('/')
def get_students():
    return student_service.get_students()


@app.get('/{name}')
def get_student_by_name(name: str):
    student = student_service.get_student_by_name(name)

    if student is None:
        return "Student with the name " + name + " doesn't exist"
    else:
        return student


@app.post('/')
def insert_student(student: Student):
    name = student.name
    surname = student.surname
    return student_service.insert_student(name, surname)


@app.put('/')
def update_student(student: Student):
    name = student.name
    surname = student.surname
    id = student.id
    if student_service.get_student_by_id(id) is None:
        return "Student with id " + id + " doesn't exist"
    return student_service.udpate_student(id, name, surname)


@app.delete('/{id}')
def delete_student(id: int):
    if student_service.delete_student_by_id(id):
        return "Student is now deleted"
    else:
        return "Student doesn't exist"
