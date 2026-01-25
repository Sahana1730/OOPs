#_init_() is special method which is first run as soon as the object is created


class job:
    def __init__(self,name,language,salary):
        self.name=name
        self.language=language
        self.salary=salary
        print("i m creating an object:")

sahana=job("shaila","python",2000000)
print(sahana.name,sahana.language,sahana.salary)

