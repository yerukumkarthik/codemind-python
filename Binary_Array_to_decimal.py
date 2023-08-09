n=int(input())
lst=list(map(int,input().split()))
st=""
for i in lst:
    st=st+str(i)
print(int(st,2))