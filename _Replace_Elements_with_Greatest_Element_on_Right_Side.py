n=int(input())
lst=list(map(int,input().split()))
for i in range(len(lst)):
    maxi=0
    if i==len(lst)-1:
        print("-1")
        break
    for j in range(i+1,len(lst)):
        if lst[j]>maxi:
            maxi=lst[j]
    print(maxi,end=" ")