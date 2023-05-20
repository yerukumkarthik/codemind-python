n=int(input())
lst=list(map(int,input().split()))
for i in lst:
    count=0
    for j in lst:
        if j<i and i!=j:
            count+=1
    print(count,end=" ")