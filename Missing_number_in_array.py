m=int(input())
for i in range(m):
    n=int(input())
    lst=list(map(int,input().split()))
    for j in range(1,max(lst)+2):
        if j not in lst:
            print(j)
            break