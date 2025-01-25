class a:
    def __init__(self):
        print("A")
    x=1
class b(a):
    def __init__(self):
        print("B")
    y=2
class c(b):
    def __init__(self):
        super().__init__()
        print("C")
    z=3



# obj=a()
# print(obj.x)
# obj=b()
# print(obj.x,obj.y)
obj=c()
print(obj.x,obj.y,obj.z)

# a--> b -->c 