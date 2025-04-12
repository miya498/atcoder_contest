N, K = map(int, input().split())
mod = 10**9
dp = [0] * (N + 1)
window = 0
for i in range(N + 1):
    if i < K:
        dp[i] = 1
        window = (window + dp[i]) % mod
    else:
        dp[i] = window % mod
        window = (window + dp[i] - dp[i - K]) % mod
print(dp[N])
