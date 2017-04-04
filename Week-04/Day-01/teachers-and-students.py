'''Create Student and Teacher classes
Student
learn()
question(teacher) -> calls the teachers answer method
Teacher
teach(student) -> calls the students learn method
answer()'''

class Student:
    def learn(self):
        pass

    def question(self, teacher):
        teacher.answer()

class Teacher:
    def __init__(self, hair):
        self.hair = hair

    def teach(self, student):
        pass

    def answer(self):
        print("answer")
        print(self.hair)

Rufusz = Student()
Geza = Teacher("black")
Bela = Teacher("brown")

Rufusz.question(Geza)
Rufusz.question(Bela)
