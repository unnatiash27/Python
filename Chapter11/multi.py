class emp:
    company="ITC"
    name="Default"

    def show(self):
        print(f"Name is {self.name}")

class coder:
    language="Python"
    def languages(self):
        print(f"Language is {self.language}")

class prog(emp,coder):
    salary=500000
    def salarys(self):
        print(f"Salary is {self.salary}")

# a=emp()
b=prog()
# c.coder()

b.show()
b.languages()
b.salarys()