N = int(input())
P = list(map(int,input().split()))

ans = 0
idx = [0]*N
for i in range(N):
    idx[P[i]] = i

dist = [0]*N

for i in range(N):
    dist[i] = (i-idx[i])%N

count = [0]*N
for i in range(N):
    count[dist[i]] += 1

ans = 0

for i in range(N):
    ans = max(ans,count[i]+count[(i+1)%N]+count[(i-1)%N])

print(ans)