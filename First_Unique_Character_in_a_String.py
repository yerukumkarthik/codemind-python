st=input()
s=0
for i in range(len(st)):
    if st.count(st[i])==1:
        s=1
        print(i)
        break
if s==0:
    print("-1")