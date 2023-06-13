num=int(input())
lst=list(map(int,input().split()))
for i in range(1,max(lst)):
    for j in lst:
        if j%i!=0:
            break
    else:
        maxi=i
print(maxi)