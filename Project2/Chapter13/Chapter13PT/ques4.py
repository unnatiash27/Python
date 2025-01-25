def fun(n):
    if(n%2 == 0):
        return True
    return False

a= [1,2,43,4,6543,554,765,21,7654]

f=list(filter(fun,a))
print(f)