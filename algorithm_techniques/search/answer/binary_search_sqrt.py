def integer_sqrt(x):
    if x < 2:
        return x
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right

# 使用例
if __name__ == "__main__":
    x = 10
    print("Integer square root of", x, "is", integer_sqrt(x))