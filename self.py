class job:
    name="harry"
    language="python"
    salary=10000
#every method we use include self even if we use it or no
    def getinfo(self):
        print(f"language is {self.language}. \n salary is {self.salary}")

    def greet(self):
        print("good morning")
result=job()
job.getinfo(result) 
job.greet(result) 
#or

# result.getinfo()

#static method
class job:
    @staticmethod
    def greet():
        print("good morning")

result=job
result.greet()
