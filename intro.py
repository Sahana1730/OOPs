#solving problem by creating object
#focuses on using reusable code(dry principle)

#class is blueprint for creating objects


#class and object creation

class job:      
    language="python"  #class attributes
    salary=100000

#object creation
obj=job()
obj.name="sahana"   #object attribute
print(obj.name,obj.language,obj.salary)

obj2=job()
obj2.name="alex"    #object attribute
obj2.place="banglore"
print(obj2.name,obj2.language,obj2.salary,obj2.place)