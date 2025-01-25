p1="click me"
p2="open this link"
p3="buy now"

msg=input("Enter messgae ")

if(p1 in msg or p2 in msg or p3 in msg):
    print("Spam")
else:
    print("Not spam")