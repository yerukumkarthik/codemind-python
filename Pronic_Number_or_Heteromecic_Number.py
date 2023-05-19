num=int(input())
s=0
i=0
while(1):
    if i>num:
        s=1
        break
    if i*(i+1)==num:
        print("YES")
        break
    i+=1
if s==1:
    print("NO")