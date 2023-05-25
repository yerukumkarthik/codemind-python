n=int(input())
lst=list(map(int,input().split()))
maxi=max(lst)+2
for i in range(1,maxi):
    if i not in lst:
        print(i)
        break