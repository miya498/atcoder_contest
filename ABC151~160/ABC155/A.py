A,B,C = map(int,input().split())

if (A == B and B != C) or (A == C and B != C) or (B == C and A != C):
    print("Yes")
else:
    print("No")