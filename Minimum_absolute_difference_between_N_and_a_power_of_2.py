num=int(input())
mini=num
for i in range(1,num):
    if abs((2**i)-num)<mini:
        mini=abs((2**i)-num)
    else:
        break
print(mini)