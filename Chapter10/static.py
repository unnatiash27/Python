class emp:
    lang="pyhon"
    salary=1500000
    def fun(self):
        print(f"language is {self.lang} and salary is {self.salary}")
    @staticmethod
    def greet():
        print("greetings from me!")


info=emp()
info.greet() 
info.fun()  #this is same as emp.fun(info)
