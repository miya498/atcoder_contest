A,B = map(int,input().split())
if B > A:
    A,B = B,A

if (A+B) % 2 != 0:
    print("IMPOSSIBLE")
else:
    print((A+B)//2)
