n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
val,s=0,0
for i in lst:
    if i not in range(a,b+1):
        print(i,end=" ")
        s=1
if s!=1:
    print("-1")