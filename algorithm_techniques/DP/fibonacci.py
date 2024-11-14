def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# 使用例
if __name__ == "__main__":
    n = 10
    print(f"Fibonacci number at position {n}:", fibonacci(n))