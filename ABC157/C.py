N,M = map(int,input().split())
S = []
C = []

for i in range(M):
    s,c = map(int,input().split())
    S.append(s)
    C.append(c)

ans = [-1]*N

for i in range(M):
    if ans[S[i]-1] == -1 or ans[S[i]-1] == C[i]:
        ans[S[i]-1] = C[i]
    else:
        print(-1)
        exit()

if ans[0] == 0 and N > 1:
    print(-1)
    exit()

for i in range(N):
    if i == 0 and ans[i] == -1 and N > 1:
        ans[i] = 1
    if i == 0 and ans[i] == -1 and N == 1:
        ans[i] = 0
    if ans[i] == -1:
        ans[i] = 0

print("".join(map(str,ans)))

