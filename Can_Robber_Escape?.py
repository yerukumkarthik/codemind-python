n=int(input())
lst=list(map(int,input().split()))
s=0
for i in lst:
    if i>=n:
        s=1
        break
if s!=1:
    print("YES")
else:
    print("NO")