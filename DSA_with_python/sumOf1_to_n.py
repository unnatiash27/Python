def fun(n):
    if n==1:
        return 1
    return n+fun(n-1)

x=fun(4)
print(x)
