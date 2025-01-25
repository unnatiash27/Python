class emp:
    company="ITC"
    def show(self):
        print(f"Name is {self.name}")
    
# class prog:
#     company="Infotech"
#     def show(self):
#         print(f"Name is {self.name}")
#     def language(self):
#         print(f"Language is {self.language}")


class prog(emp):  #inheritance
    company="Infotech"
    def language(self):
        print(f"Language is {self.language}")

a=emp()
b=prog()

print(a.company,b.company)