def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
num=int(input())
if num==1:
    print("Not Mega Prime")
elif is_prime(num):
    for i in str(num):
        if not is_prime(int(i)):
            print("Not Mega Prime")
            break
    else:
        print("Mega Prime")
else:
    print("Not Mega Prime")