#instance attribute take over class attribute if both have same name

class job:
    language="python"  #class attributes
    salary=100000

obj=job()
obj.language="java"   #instance attribute
print(obj.language,obj.salary)  #java 100000


#self parameter is used to refer to instance attributes
obj2=job()
print(obj2.language,obj2.salary)  #python 100000
#class attribute remains same for other objects unless modified
