f=open("poem.txt", "r")
c=f.read()
if("twinkle"in c):
    print ("Present")
else:
    print ("Absent")
f.close()