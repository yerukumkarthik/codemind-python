num=int(input())
s=0
for i in range(num):
    if i*(i+1)==num:
        s=1
        print("YES")
        break
if s==0:
    print("NO")