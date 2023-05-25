n=int(input())
lst=list(map(int,input().split()))
lst1=list(map(int,input().split()))
for i in range(n):
    print(lst[i]+lst1[i],end=" ")