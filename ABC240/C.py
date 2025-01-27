N,X = map(int,input().split())
A,B = [],[]
for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

dp = [[False]*(X+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
    for x in range(X+1):
        if x-A[i] >= 0 and dp[i][x-A[i]]:
            dp[i+1][x] = True
        if x-B[i] >= 0 and dp[i][x-B[i]]:
            dp[i+1][x] = True

if dp[N][X]:
    print("Yes")
else:
    print("No")