# 入力の受け取り
grid = [list(input()) for _ in range(4)]

# 180度回転
rotated_grid = [row[::-1] for row in grid[::-1]]

# 出力
for row in rotated_grid:
    print("".join(row))