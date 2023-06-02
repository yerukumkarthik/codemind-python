nu=int(input())
lst=list(map(int,input().split()))
esu=0
osu=0
for i in range(len(lst)):
    if i%2==1:
        osu+=lst[i]
    else:
        esu+=lst[i]
print(abs(osu-esu))