A, B = map(int,input().split())

if A-B == 0:
    print(1)
elif (A-B) % 2 == 1:
    print(2)
else:
    print(3) 