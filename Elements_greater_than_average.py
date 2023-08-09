n=int(input())
lst=list(map(int,input().split()))
avg=sum(lst)//len(lst)
c=0
for i in lst:
    if avg<=i:
        c+=1
print(c)