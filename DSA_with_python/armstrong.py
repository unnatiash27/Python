
def fun(n): 
    num=n
    t=0
    l=len(str(num))
    while num>0:
        d=num%10
        t=t+(d**l)
        num=num//10
    if n==t:
        return True
    return False
n=int(input("Enter a number"))
x=fun(n)
print(x)
