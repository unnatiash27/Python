arr=[5,7,8,4,1,6,9,2]

def merge(l,r):
    res=[]
    i,j=0,0
    n,m=len(l),len(r)
    while i<n and j<m:
        if l[i]<=r[j]:
            res.append(l[i])
            i+=1
        else:
            res.append(r[j])
            j+=1
    if i<n:
        res.append(l[i])
        i+=1
    if j<m:
        res.append(r[j])
        j+=1
    return res

def devide(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    l=devide(left)
    r=devide(right)
    return merge(l,r)

sorted_arr = devide(arr)
print(sorted_arr)