class emp:
    lang="pyhon"
    salary=1500000
    def fun(self):
        print(f"language is {self.lang} and salary is {self.salary}")
    def __init__(self):
        print("This is a constructorrrr no need to calll it")
    

info=emp()
info.fun()  #this is same as emp.fun(info)
