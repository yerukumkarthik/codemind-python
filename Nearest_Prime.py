def le_prime(num):
    while(num):
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                break
        else:
            return num
        num-=1
def ri_prime(num):
    num+=1
    while(num):
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                break
        else:
            return num
        num+=1
t=int(input())
for i in range(t):
    n=int(input())
    le=le_prime(n)
    ri=ri_prime(n)
    if abs(le-n)>abs(ri-n):
        print(ri)
    elif abs(le-n)<abs(ri-n):
        print(le)
    else:
        print(le)