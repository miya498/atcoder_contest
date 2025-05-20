N,M = map(int,input().split())
A = [False]*(N+1)
for i in range(M):
    a = int(input())
    A[a] = True

dp = [0]*(N+1)
dp[0] = 1

for i in range(1,N+1):
    if A[i]:
        dp[i] = 0
    else:
        if i >= 2:
            dp[i] = (dp[i-1]+dp[i-2])%1000000007
        else:
            dp[i] = dp[i-1]

print(dp[N]%1000000007)
