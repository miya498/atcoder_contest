def single_element(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if mid % 2 == 1:
            mid -= 1
        if arr[mid] == arr[mid + 1]:
            left = mid + 2
        else:
            right = mid
    return arr[left]

# 使用例
if __name__ == "__main__":
    arr = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    print("Single element is:", single_element(arr))