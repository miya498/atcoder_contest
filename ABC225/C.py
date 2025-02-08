N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

# B[0][0] が A の何行目に該当するか
start_row = (B[0][0] - 1) // 7
start_col = (B[0][0] - 1) % 7

# 切り出した範囲が 7列の範囲を超えないかチェック
if start_col + M > 7:
    print("No")
    exit()

# 行の検証
for i in range(N):
    for j in range(M):
        expected_value = (start_row + i) * 7 + (start_col + j + 1)
        if B[i][j] != expected_value:
            print("No")
            exit()

print("Yes")