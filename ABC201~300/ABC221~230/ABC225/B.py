from collections import defaultdict

N = int(input())
graph = defaultdict(list)

for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    if len(graph[i]) == N-1:
        print("Yes")
        exit()
print("No")
