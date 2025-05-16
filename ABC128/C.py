N,M = map(int,input().split())
switch = [[] for _ in range(N)]
for i in range(M):
    A = list(map(int,input().split()))
    for j in A[1:]:
        switch[j-1].append(i)

P = list(map(int,input().split()))

ans = 0
for i in range(2**N):
    light = [0]*M
    flag = True
    for j in range(N):
        if i & (1<<j):
            for k in switch[j]:
                light[k] += 1
    for j in range(M):
        if light[j] % 2 != P[j]:
            flag = False
            break
    if flag:
        ans += 1

print(ans)
