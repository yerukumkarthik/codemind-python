num=input()
sq=int(num)**2
auto=str(sq)[len(str(sq))-len(num)::1]
if num==auto:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")