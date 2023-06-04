n=int(input())
lst=list(map(int,input().split()))
num=int(input())
val=0
for i in lst:
    if i==num:
        val+=1
print(val)