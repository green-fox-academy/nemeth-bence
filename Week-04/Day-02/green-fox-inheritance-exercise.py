class Person():

    def __init__(self, name = "Jane Doe", age = 30, gender = "female"):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Hi, I'm " + str(self.name) + ", a " + str(self.age) + " year old " + str(self.gender)+".")

    def get_goal(self):
        print("My goal is: Live for the moment!")

class Student(Person):

    def __init__(self, name = "Jane Doe", age = 30, gender = "female", previous_organization = "The School of Life", skipped_days = 0):
        super().__init__(name, age, gender)
        self.previous_organization = previous_organization
        self.skipped_days = skipped_days

    def get_goal(self):
            print("Be a junior software developer.")

    def introduce(self):
        print("Hi, I'm " + str(self.name) + ", a " + str(self.age) + " year old " + str(self.gender)+" from " + str(self.previous_organization) + " who skipped " + str(self.skipped_days) + " days from the course already.")

    def skip_days(self, number_of_days):
        self.skipped_days += number_of_days

class Mentor(Person):

    def __init__(self, name = "Jane Doe", age = 30, gender = "female", level = "intermediate"):
        super().__init__(name, age, gender)
        self.level = level

    def get_goal(self):
            print("Educate brilliant junior software developers.")

    def introduce(self):
        print("Hi, I'm " + str(self.name) + ", a " + str(self.age) + " year old " + str(self.gender) + " " + str(self.level) + " mentor.")

class Sponsor(Person):

    def __init__(self, name = "Jane Doe", age = 30, gender = "female", company = "Google", hired_students = 0):
        super().__init__(name, age, gender)
        self.company = company
        self.hired_students = hired_students

    def introduce(self):
        print("Hi, I'm " + str(self.name) + ", a " + str(self.age) + " year old " + str(self.gender) + " who represents " + str(self.company) + " and hired " + str(self.hired_students) + " students so far.")

    def get_goal(self):
            print("Hire brilliant junior software developers.")

    def hire(self):
        self.hired_students += 1

Liz=Sponsor()
print(Liz.hire())
