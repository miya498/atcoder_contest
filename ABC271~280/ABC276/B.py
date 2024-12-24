N,M = map(int,input().split())

ans = [[] for _ in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    ans[a-1].append(b)
    ans[b-1].append(a)

for i in range(N):
    ans[i].sort()
    print(len(ans[i]),*ans[i])

    