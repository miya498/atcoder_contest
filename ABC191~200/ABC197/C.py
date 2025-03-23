N = int(input())
A = list(map(int, input().split()))

# 答えの初期値（十分大きな値）
ans = 10**18

# 区間の切り方は、N-1 個の区切り位置の有無をビットマスクで表現
# mask の各ビット i (0-indexed) は、位置 i と i+1 の間に切り目があるかを表す
for mask in range(1 << (N - 1)):
    cur_or = A[0]  # 現在の区間の OR 値
    cur_xor = 0    # これまでの区間の OR の XOR 値
    for i in range(N - 1):
        # i 番目のビットが立っているなら、区間を切る
        if mask & (1 << i):
            cur_xor ^= cur_or  # これまでの区間の OR 値を XOR に加算
            cur_or = A[i + 1]   # 新たな区間の開始
        else:
            # 区間を延長して OR を更新
            cur_or |= A[i + 1]
    # 最後の区間の OR 値を XOR に加える
    cur_xor ^= cur_or
    # 最小値の更新
    if cur_xor < ans:
        ans = cur_xor

print(ans)