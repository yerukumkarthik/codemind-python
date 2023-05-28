a=int(input())
b=int(input())
s=0
for i in range(a,b+1):
    s=0
    if '0' in str(i):
        continue
    for j in str(i):
        if i%int(j)!=0:
            s=1
            break
    if s!=1:
        print(i,end=" ")