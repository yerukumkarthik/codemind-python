num=input()
ev=0
od=0
for i in num:
    if(int(i)%2==0):
        ev=1
    elif int(i)%2==1:
        od=1
if ev==1 and od==1:
    print("Mixed")
elif ev==1 and od!=1:
    print("Even")
else:
    print("Odd")