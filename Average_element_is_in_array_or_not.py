nu=int(input())
lst=list(map(int,input().split()))
num=sum(lst)//len(lst)
print(num in lst)