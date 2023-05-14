def is_notprime(a):
    c=0
    for i in range(1,a):
        if(a%i==0):
            c+=1;
    return c>1
num=int(input())
count=0
for i in range(1,num+1):
    if(num%i==0 and is_notprime(i)):
        count+=1
print(count+1)