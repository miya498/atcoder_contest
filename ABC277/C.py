from collections import deque

N = int(input())
edges = {}

for _ in range(N):
    A, B = map(int, input().split())
    if A not in edges:
        edges[A] = []
    if B not in edges:
        edges[B] = []
    edges[A].append(B)
    edges[B].append(A)

visited = set()
queue = deque([1]) 
visited.add(1)
max_floor = 1

while queue:
    current = queue.popleft()
    max_floor = max(max_floor, current)
    for neighbor in edges.get(current, []):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

print(max_floor)