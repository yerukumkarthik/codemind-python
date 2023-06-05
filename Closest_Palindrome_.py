def bef_pal(num):
    while(num):
        num-=1
        if str(num)==str(num)[::-1]:
            return num
def aft_pal(num):
    while(num):
        num+=1
        if str(num)==str(num)[::-1]:
            return num
num=int(input())
bef=bef_pal(num)
aft=aft_pal(num)
if abs(bef-num)>abs(aft-num):
    print(aft)
elif abs(bef-num)<abs(aft-num):
    print(bef)
elif abs(bef-num)==abs(aft-num):
    print(bef,aft)