A,B,C,D = map(int,input().split())

while A > 0 or C > 0:
    C -= B
    if C <= 0:
        break
    A -= D
if A <= 0:
    print("No")
else:
    print("Yes")