a=int(input("Enter the number"))
b=int(input("Enter the number"))

if(b==0):
    raise ZeroDivisionError("Invalid no.")
else:
    print(f"Ans is {a/b}")