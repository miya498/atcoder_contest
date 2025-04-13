N,M,Q = map(int,input().split())
P = []
for _ in range(Q):
    a,b,c,d = map(int,input().split())
    P.append([a,b,c,d])

ans = 0

def dfs(idx,seq):
    global ans
    if idx == N:
        score = 0
        for a,b,c,d in P:
            if seq[b-1] - seq[a-1] == c:
                score += d
        ans = max(ans,score)
        return
    if seq:
        start = seq[-1]
    else:
        start = 1
    for num in range(start,M+1):
        dfs(idx+1,seq+[num])
dfs(0,[])
print(ans)
