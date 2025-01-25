def fun(n):
    c=0
    while n>0:
        c+=1
        n=n//10
    print(c)


n=int(input("Enter a number"))
fun(n)