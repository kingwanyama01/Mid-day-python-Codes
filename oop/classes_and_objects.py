class Student:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password

    def register(self):
        print("You used",self.email,"to register")

    def login(self):
        if self.email == "e@gmail.com" and self.password == "123":
            print("Login successful")
        else:
            print("Wrong email or password")


studentOne = Student("Emmanuel","e@gmail.com","123")
studentTwo = Student("Samson","s@gmail.com","12345")

studentOne.login()
studentTwo.login()

print(studentTwo.name)



class Teacher(Student):
    def uploadResults(self):
        print("Yeah, I can upload results")

teacherOne = Teacher("King","k@gmail.com","123")
teacherOne.login()
teacherOne.uploadResults()


class Moja:
    def moja(self):
        print("Moja")
class Mbili:
    def mbili(self):
        print("Mbili")
class Tatu(Moja,Mbili):
    pass


nambari = Tatu()
nambari.moja()
nambari.mbili()

