def prnt_fact(n):
    pro=1
    for i in range(1,n+1):
        pro*=i
    print(pro)
t=int(input())
for i in range(t):
    num=int(input())
    prnt_fact(num)