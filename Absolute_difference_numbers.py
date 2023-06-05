n,di=map(str,input().split())
fi=n[0:int(di)]
la=n[-int(di)::1]
print(abs(int(fi)-int(la)))