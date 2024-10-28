A,B,C = map(int,input().split())

ans = True

if B<C:
    if B<=A and A<=C:
        ans = False
else:
    C+=24
    if (B<=A and A<=C) or (B<=A+24 and A+24<=C):
        ans = False

if ans:
    print("Yes")
else:
    print("No")

