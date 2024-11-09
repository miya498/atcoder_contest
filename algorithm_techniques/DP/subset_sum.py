def subset_sum(nums, target):
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for j in range(target + 1):
            if j >= nums[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
                
    return dp[n][target]

# 使用例
if __name__ == "__main__":
    nums = [3, 34, 4, 12, 5, 2]
    target = 9
    print("Subset with sum exists:", subset_sum(nums, target))
