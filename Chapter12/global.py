a=32  #global var

def fun():
    global a
    a=2  #local variable
    print(a)


fun()
print(a)
