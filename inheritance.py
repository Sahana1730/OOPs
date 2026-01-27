class teacher:
    college="pu"
    def show(self):
        print("the name of the teacher is {self.name}")

#inherit
class student(teacher):
    college="presidency"
    def show(self):
        print("the name of the teacher is {self.name}")

a=teacher()
b=student()
print(a.college,b.college)