class hod:
     department="cai"
     def __init__(self, name,age):
        self.name = name
        self.age=age
        
     def show(self):
         print(f"name of hod is:{self.name},age of hod is:{self.age}")

class cc(hod):
    department="cse"
    def show(self):
        print(f"cc name is :{self.name},age of cc is:{self.age}")

class cr(hod):
    department="csn"
    def show(self):
        print(f"name of cr is:{self.name},age of cr is:{self.age}")

class student(hod):
    department="cai"
    def show(self):
        print(f"name of student is:{self.name},age of student is:{self.age}")

a=hod("zafar",45)
b=cc("yamanppa",35)
c=cr("bharath",21)
d=student("sahana",20)
print(a.department,b.department,c.department)
a.show()
b.show()
c.show()
d.show()

    