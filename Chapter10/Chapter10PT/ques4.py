from random import randint

class train:
    def __init__(self,tn):
        self.tn = tn
    def book(self):
        print(f" Train {self.tn} is booked!")
    def stat(self):
        print(f"Tain is running on time!") 
    def fare(self,fro,to):
        print(f"Fare from {fro} to {to} is {randint(222,5555)}")


t=train(12345)
t.book()
t.stat()
t.fare("goa","pune")