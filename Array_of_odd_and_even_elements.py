n=int(input())
lst=list(map(int,input().split()))
for i in lst:
    if i%2==1:
        print(i,end=" ")
for i in lst:
    if i%2==0:
        print(i,end=" ")