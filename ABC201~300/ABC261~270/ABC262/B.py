N,M = map(int,input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

ans = 0

for a in range(N):
    for b in range(a+1,N):
        for c in range(b+1,N):
            if b in graph[a] and c in graph[b] and a in graph[c]:
                ans += 1

print(ans)