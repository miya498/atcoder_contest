N = int(input())
ans = [[0]*i for i in range(1,N+1)]
for i in range(N):
    for j in range(i+1):
        if j == 0 or j == i:
            ans[i][j] = 1
        else:
            ans[i][j] = ans[i-1][j-1]+ans[i-1][j]

for i in range(N):
    print(*ans[i])

