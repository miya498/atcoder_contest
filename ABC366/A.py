N,T,A = map(int,input().split())

sabun = N-T-A

if T > A:
    if A+sabun > T:
        print("No")
    else:
        print("Yes")
else:
    if T+sabun > A:
        print("No")
    else:
        print("Yes")