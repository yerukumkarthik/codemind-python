def prime(val):
    count=0
    for i in range(1,val):
        if(val%i==0):
            count+=1
    if count<2:
        print(val)
a=int(input())
b=int(input())
for i in range(a,b+1):
    if i!=1:
        prime(i)