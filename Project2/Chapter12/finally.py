def fun():
    try:
        a=int(input("Number- "))
        print (a)
    except Exception as e:
        print(e)
    finally:
        print("Inside finally")

fun()


# finally work with function even if return there but finallyy work alwys 