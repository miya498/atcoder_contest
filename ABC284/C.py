from collections import defaultdict

def count_connected_components(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)

    def dfs(node):
        stack = [node]
        while stack:
            curr = stack.pop()
            for neighbor in graph[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

    count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            count += 1
            visited[i] = True
            dfs(i)
    return count

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

print(count_connected_components(n, edges))