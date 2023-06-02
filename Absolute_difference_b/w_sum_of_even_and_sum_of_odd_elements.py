nu=int(input())
lst=list(map(int,input().split()))
esu=0
osu=0
for i in lst:
    if i%2==1:
        osu+=i
    else:
        esu+=i
print(abs(osu-esu))