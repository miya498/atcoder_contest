A = [list(map(int, input().split())) for _ in range(9)]

flag = True

# 各行をチェック
for i in range(9):
    row_set = set()
    for j in range(9):
        row_set.add(A[i][j])
    if len(row_set) != 9:
        flag = False

# 各列をチェック
for j in range(9):
    col_set = set()
    for i in range(9):
        col_set.add(A[i][j])
    if len(col_set) != 9:
        flag = False

# 各3x3ブロックをチェック
for i in range(3):
    for j in range(3):
        block_set = set()
        for x in range(3):
            for y in range(3):
                block_set.add(A[i*3 + x][j*3 + y])
        if len(block_set) != 9:
            flag = False

# 結果を出力
if flag:
    print("Yes")
else:
    print("No")