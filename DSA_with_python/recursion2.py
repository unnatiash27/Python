c=0

def fun():
    global c
    if c==4:
        return
    else:
        c+=1
        fun()
        print("Helloo")


fun()