class Student:
    id: int
    name: str
    surname: str

    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getSurname(self):
        return self.surname

    def setSurname(self, surname):
        self.surname = surname

    def setId(self, id):
        self.id = id

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname
        }
