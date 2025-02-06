N = int(input())
T = [0]*(N+1)
graph = [[] for _ in range(N+1)]

for i in range(1,N+1):
    data = list(map(int,input().split()))
    T[i] = data[0]
    graph[i] = data[2:]

visited = set()

def dfs(v):
    if v in visited:
        return 0
    visited.add(v)
    total_time = T[v]
    for w in graph[v]:
        total_time += dfs(w)
    return total_time

print(dfs(N))
