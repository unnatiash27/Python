dic={
    "abs":33,
    "hse":90,
    "nhf":60,
    0:"hay"
}
# print(dic.items())
# print(dic.keys())
# print(dic.values())
# Updating the dictionary
print(dic.update({"nhf": 88, "renu": 100}))
# Prints None because update() modifies the dictionary in place and doesn't return anything
# Check the updated dictionary
print(dic)
print(dic.get("nhf"))#this give none if key do not exist
print(dic["nhf"]) #this give error if key do not exist
