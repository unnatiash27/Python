arr=[5,7,8,4,1,3,6,9,2]

def par(arr,l,h):
    pvt=arr[l]
    i=l
    j=h
    while i<j:
        while arr[i]<=pvt and i<=h-1:
            i+=1
        while arr[j]>pvt and j>=l+1:
            j -=1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[l],arr[j] = arr[j],arr[l]
    return j

def quick(arr,l,h):
    if l<h:
        idx=par(arr,l,h)
        quick(arr,l,idx-1)
        quick(arr,idx+1,h)

quick(arr,0,len(arr)-1)
print (arr)
        