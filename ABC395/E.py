import heapq

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
rev_graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    rev_graph[v].append(u)

dist = [[float('inf')] * 2 for _ in range(n+1)]
dist[1][0] = 0

queue = [(0, 1, 0)]

while queue:
    cost, v, state = heapq.heappop(queue)

    if cost > dist[v][state]:
        continue

    curr_graph = graph if state == 0 else rev_graph

    for next_v in curr_graph[v]:
        if dist[next_v][state] > cost + 1:
            dist[next_v][state] = cost + 1
            heapq.heappush(queue, (cost + 1, next_v, state))

    next_state = 1 - state
    if dist[v][next_state] > cost + x:
        dist[v][next_state] = cost + x
        heapq.heappush(queue, (cost + x, v, next_state))

result = min(dist[n][0], dist[n][1])
print(result)