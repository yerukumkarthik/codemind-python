num=int(input())
while(1):
    if num==1:
        print("Ugly Number")
        break
    elif num%2==0:
        num=num//2
    elif num%3==0:
        num=num//3
    elif num%5==0:
        num=num//5
    else:
        print("Not Ugly Number")
        break