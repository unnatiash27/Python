arr=[5,7,8,4,1,6,9,2]
def fun():
    n=len(arr)
    for i in range(0,n):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i]


fun()
print(arr)