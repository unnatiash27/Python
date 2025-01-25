class emp:
    lang="pyhon"
    salary=1500000
    def fun(self):
        print(f"language is {self.lang} and salary is {self.salary}")
    def greet(self):
        print("greetings")


info=emp()
info.greet() 
info.fun()  #this is same as emp.fun(info)
