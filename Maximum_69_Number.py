num=input()
s=0
for i in num:
    if i=='6' and s==0:
        s=1
        print("9",end="")
    else:
        print(i,end="")