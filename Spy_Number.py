num=int(input())
su=0
pro=1
while num>0:
    b=num%10
    su+=b
    pro*=b
    num=num//10
if su==pro:
    print("Spy Number")
else:
    print("Not Spy Number")