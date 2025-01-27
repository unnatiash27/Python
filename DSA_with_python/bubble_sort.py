arr=[1, 2, 4, 5, 6, 7, 8, 9]

def fun():
    n=len(arr)
    for i in range(n-2,-1,-1):
        sw=False
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                sw=True
                arr[j],arr[j+1] = arr[j+1],arr[j]
        if sw==False:
                break

# print(arr)
fun()
print(arr)
