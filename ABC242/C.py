N = int(input())
MOD = 998244353

dp = [[0] * 10 for _ in range(N + 1)]

# 初期条件
for j in range(1, 10):
    dp[1][j] = 1

# 遷移
for i in range(1, N):
    for j in range(1, 10):
        if j > 1:
            dp[i + 1][j - 1] += dp[i][j]
            dp[i + 1][j - 1] %= MOD
        dp[i + 1][j] += dp[i][j]
        dp[i + 1][j] %= MOD
        if j < 9:
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j + 1] %= MOD

# 結果
print(dp)
print(sum(dp[N]) % MOD)