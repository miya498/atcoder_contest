from collections import Counter, defaultdict

N,M = map(int,input().split())
C = list(input().split())
D = list(input().split())
D_dict = defaultdict(int)
P = list(map(int,input().split()))

for i in range(M):
    D_dict[D[i]] += P[i+1]

ans = 0
for i in range(N):
    if C[i] not in D:
        ans += P[0]
    else:
        ans += D_dict[C[i]]

print(ans)