N,M = map(int,input().split())
S = [int(input()) for i in range(N)]
T = [int(input()) for i in range(M)]
ans = 0

for i in range(N):
    for j in range(M):
        if S[i]%1000 == T[j]:
            ans += 1
            break

print(ans)