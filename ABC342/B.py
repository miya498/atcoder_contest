N = int(input())
P = list(map(int,input().split()))
Q = int(input())

for __ in range(Q):
    A,B = map(int,input().split())
    a=0
    b=0
    for i in range(N):
        if A == P[i]:
            a = i+1
        elif B == P[i]:
            b = i+1
    if  a>b:
        print(B)
    else:
        print(A)