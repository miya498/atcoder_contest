A,B = map(int,input().split())

if (A%3 == 2 and B-A == 1) or (A%3 == 1 and B-A == 1):
    print("Yes")
else:
    print("No")