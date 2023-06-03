n=int(input())
lst=list(map(int,input().split()))
for i in range(n):
    if lst[i]%2==1:
        val=i
print(val)