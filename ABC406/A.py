A,B,C,D = map(int,input().split())

if A > C:
    print("Yes")
elif A == C and D <= B:
    print("Yes")
else:
    print("No")
