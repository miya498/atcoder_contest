N,M = map(int,input().split())
S = list(input().split())
T = list(input().split())

m = 0
for i in range(N):
    if S[i] == T[m]:
        print("Yes")
        m += 1
    else:
        print("No")
