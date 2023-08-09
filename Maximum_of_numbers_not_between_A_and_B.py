n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
maxi=0
s=0
for i in lst:
    if i not in range(a,b+1):
        if i>maxi:
            maxi=i
            s=1
if s!=1:
    print("-1")
else:
    print(maxi)