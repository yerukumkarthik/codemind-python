num=input()
if num[0]=='-':
    print("-",end="")
    for i in num[:-len(num):-1]:
        if i!='0':
            print(i,end="")
elif '0' not in num[len(num)-1]:
    print(num[::-1])
else:
    for i in num[::-1]:
        if i!='0':
            print(i,end="")