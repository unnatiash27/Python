import random

def game():
    print("You are playing....")
    s=random.randint(1,50)
    #fetch hs
    with open("hs.txt","r") as f:
        hs=f.read()
        if(hs!=""):
            hs=int(hs)
        else:
            hs=0
        
        print(f"Score is - {s}")
        if(s>hs):
            #write high score
            with open("hs.txt","w") as f:
                f.write(str(s))
        
        return s

game()