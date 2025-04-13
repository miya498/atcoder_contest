N,M = map(int,input().split())
H = list(map(int,input().split()))
path = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    path[a-1].append(b-1)
    path[b-1].append(a-1)

ans = 0
for i in range(N):
    flag = True
    for j in path[i]:
        if H[i] <= H[j]:
            flag = False
    if flag:
        ans += 1

print(ans)
