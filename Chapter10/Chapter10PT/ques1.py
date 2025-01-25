class prog:
    company="Microsoft Corporation"
    def __init__(self,name,sal,pin):
        self.name = name
        self.sal = sal
        self.pin = pin

p=prog("Unnati",2500000,67234)
print(p.name,p.sal,p.pin,p.company)

r=prog("Shriya",2100000,67834)
print(r.name,r.sal,r.pin,r.company)