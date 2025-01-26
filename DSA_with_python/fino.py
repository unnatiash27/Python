def fun(n):
    if n==0 or n==1:
        return n
    return fun(n-1)+fun(n-2)

n=int(input("Number is- "))
ans=fun(n)
print(ans)