def prime_check(val):
    count=0
    for i in range(1,val):
        if(val%i==0):
            count+=1
    return count<2
n1=int(input())
n2=int(input())
su=n1+n2
i=1
while(1):
    if(prime_check(su+i)):
        print(i)
        break
    i+=1