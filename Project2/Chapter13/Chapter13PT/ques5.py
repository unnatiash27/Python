from functools import reduce
l= [1,2,43,4,45,82,87,21,87]
def fun(a,b):
    if(a>b):
        return a
    return b

print(reduce(fun,l))