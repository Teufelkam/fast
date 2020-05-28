from student import Student



class Student_Service:
    students = [Student(1, "Oleksandr", "Tsyhanovych"), Student(2, "John", "Smith"), Student(3, "Alex", "Jackson")]

    def __init__(self) -> None:
        super().__init__()

    def get_students(self):
        return self.students

    def get_student_by_id(self, id):
        for student in self.students:
            if student.id == id:
                return student

    def get_student_by_name(self, name):
        for student in self.students:
            if student.name == name:
                return student

    def insert_student_object(self, student: Student):
        id = self.generate_id(student.id)
        student.setId(id)
        self.students.append(student)
        return student

    def insert_student(self, name, surname):
        student = Student(0, name, surname)
        return self.insert_student_object(student)

    def udpate_student(self, id, name, surname):
        student = self.get_student_by_id(id)
        student.setName(name)
        student.setSurname(surname)
        return self.get_student_by_id(id)

    def delete_student_by_id(self, id):
        student = self.get_student_by_id(id)
        if student is not None:
            self.students.remove(student)
            return True
        else:
            return False

    def generate_id(self, id=0):
        ids = list(map(lambda student: int(student.id), self.students))
        print(ids)
        print(id)
        if isinstance(id, int):
            new_id = id
        else:
            new_id = 0

        while new_id in ids:
            new_id += 1

        return new_id


