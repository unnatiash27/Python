n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,6,7,2]

# brute force
def brute_force():
    res=[]
    for i in m:
        c=0
        for j in n:
            if i==j:
                c+=1
        res.append(c)
    return res

def optimal():
    hash=[0]*11
    for i in n:
        hash[i]+=1
    for j in m:
        if j<1 or j>11:
            print(0)
        else:
            print(hash[j])

# ans = brute_force()
ans = optimal()
print(f"Occurrences of each item in m within n: {ans}")
