import random
n=random.randint(1,100)
a=-1
gus=0
while(a!=n):
    gus+=1
    a=int(input("Guess a number"))
    if(a>n):
        print("Go Lower")
    else:
        print("Go Upper")


print(f"You Gussed it right in {gus} attempt !!!!")


