A,B,C = map(int,input().split())

if (A == B and B == C) or (A+B == C) or (A+C == B) or (B+C == A):
    print("Yes")
else:
    print("No")