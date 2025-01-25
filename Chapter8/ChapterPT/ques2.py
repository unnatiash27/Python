def feh(x):
    c=5*(x-32)/9
    return c
x=int(input("Enter value: "))
c=feh(x)
print(f"{round(c,2)} deg C")