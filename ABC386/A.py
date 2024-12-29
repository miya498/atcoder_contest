A,B,C,D = map(int,input().split())
fullhouse = set()
fullhouse.add(A)
fullhouse.add(B)
fullhouse.add(C)
fullhouse.add(D)

if len(fullhouse) == 2:
    print("Yes")
else:
    print("No")
