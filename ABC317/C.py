from collections import defaultdict

N,M = map(int,input().split())
graph = defaultdict(list)

for _ in range(M):
    A,B,C = map(int,input().split())
    graph[A].append((B,C))
    graph[B].append((A,C))

def dfs(node, visited):
    visited.add(node)
    max_dict = 0
    for neighbor, distance in graph[node]:
        if neighbor not in visited:
            max_dict = max(max_dict,distance+dfs(neighbor,visited))
    visited.remove(node)
    return max_dict

ans = 0
for start_node in range(1,N+1):
    ans = max(ans,dfs(start_node,set()))

print(ans)
