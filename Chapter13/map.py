
from functools import reduce

# map
l=[32,43,7,34,322,77]
sq=lambda x: x*x 

sql=map(sq,l)
print (list(sql))


# filter
def fun(n):
    if(n%2==0):
        return True
    return False

o=filter(fun,l)
print(list(o))


# reduce
def sum(a,b):
    return a+b

mul = lambda x,y: x*y


print(reduce(sum,l))
print(reduce(mul,l))