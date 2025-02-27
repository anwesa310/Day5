class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def showName(self):
        print("Name:",self.name)
    def showAge(self):
        print("Age:",self.age)
class Student(Person):
    def __init__(self,n,a,r):
        super().__init__(n,a,)
        self.rollno=r
    def showRoll(self):
        print("Roll no.:",self.rollno)
s1=Student("Anwesa",20,22)
s1.showName()
s1.showAge()
s1.showRoll()