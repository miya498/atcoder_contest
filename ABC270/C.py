from collections import deque

N,X,Y = map(int,input().split())
graph = [[] for _ in range(N)]

for i in range(N-1):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

q = deque()
q.append(X-1)
upper = [-1]*N
#-2は頂点
upper[X-1] = -2

def BFS():
    while q:
        now = q.popleft()
        for n in graph[now]:
            if upper[n] == -1:
                upper[n] = now
                q.append(n)

BFS()

ans = []
now = Y-1

while upper[now] != -2:
    ans.append(now)
    now = upper[now]

ans.append(now)

for i in ans[::-1]:
    print(i+1,end=" ")
