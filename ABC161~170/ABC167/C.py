N,M,X = map(int,input().split())
C = [list(map(int,input().split())) for _ in range(N)]
ans = 10000000
for bit in range(2**N):
    result = [0]*(M+1)
    for i in range(N):
        if (bit & (1<<i)):
            for j in range(M+1):
                result[j] += C[i][j]
    flag = True
    for i in range(1,M+1):
        if result[i] < X:
            flag = False

    if flag:
        ans = min(ans,result[0])

if ans == 10000000:
    print(-1)
else:
    print(ans)