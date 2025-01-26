num=[2,5,2,7,4,8,1,9,4,8,0]
def fun(num,l,r):
    if l>=r:
        return
    num[l],num[r] = num[r],num[l]
    fun(num,l+1,r-1)

l=0
r=len(num)-1
fun(num,l,r)
print (num)