nums=[1,4,2,7,3,3,3,8,2,7,1,3,]
freq=dict()

for i in range(0,len(nums)):
    freq[nums[i]]=freq.get(nums[i],0)+1

# method 1
# for i in range(0,len(nums)):
#     if nums[i] in freq:
#         freq[nums[i]]+=1
#     else:
#         freq[nums[i]]=1

print(freq[3])
