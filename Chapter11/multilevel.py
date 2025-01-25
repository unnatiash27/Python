class a:
    x=1
class b(a):
    y=2
class c(b):
    z=3

obj=a()
print(obj.x)
obj=b()
print(obj.x,obj.y)
obj=c()
print(obj.x,obj.y,obj.z)

# a--> b -->c 