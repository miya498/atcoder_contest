N,X = map(int,input().split())

L = []
for _ in range(N):
    bool = list(map(int,input().split()))
    a = bool[1:]
    L.append(a)

def dfs(pos,seki):
    if pos == N:
        if seki == X:
            return 1
        else:
            return 0
    ans = 0
    for i in L[pos]:
        if seki*i > X:
            continue
        ans += dfs(pos+1,seki*i)
    return ans

print(dfs(0,1))
