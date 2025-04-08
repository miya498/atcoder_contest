N,K = map(int,input().split())
D = [0]*N

for _ in range(K):
    d = int(input())
    A = list(map(int,input().split()))
    for a in A:
        D[a-1] += 1
ans = 0
for i in range(N):
    if D[i] == 0:
        ans += 1
print(ans)