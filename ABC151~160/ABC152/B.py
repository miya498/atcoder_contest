a,b = map(int,input().split())

A = ""
for i in range(b):
    A += str(a)
B = ""
for i in range(a):
    B += str(b)


if A < B:
    print(A)
else:
    print(B)
