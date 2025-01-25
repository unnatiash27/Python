n= 3683

tb=[n*i for i in range (1,11)]

with open("tb.txt","a")as f:
    f.write(str(tb)+ "\n")