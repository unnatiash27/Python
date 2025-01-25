
def fun(n):
    num=n
    res=0
    while num>0:
        d=num%10
        res=(res*10)+d
        num=num//10
    if res==n:
        return True
    else:
        return False

n=int(input("Enter a number"))
x=fun(n)
print(x)
