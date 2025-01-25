from math import sqrt

def fun(n):
    res=[]
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            res.append(i)
        if n//i != i:
            res.append(n//i)
    # res.append(n)
    res.sort()
    return res

n=int(input("Enter a number- "))
x=fun(n)
print(x)
