class emp:
    lang="pyhon"
    salary=1500000
    def fun(self):
        print(f"language is {self.lang} and salary is {self.salary}")
    def __init__(self,name,lang,salary):
        self.name = name
        self.lang = lang
        self.salary = salary
        print("This is a constructorrrr no need to calll it")
    

info=emp("rini","JS",1800000)
print(info.name,info.lang,info.salary)
# info.fun()  this is same as emp.fun(info)

