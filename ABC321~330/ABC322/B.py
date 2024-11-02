N,M = map(int,input().split())
S = input()
T = input()

if S == T[:N]:
    if S == T[M-N:M]:
        print(0)
    else:
        print(1)
else:
    if S == T[M-N:M]:
        print(2)
    else:
        print(3)


