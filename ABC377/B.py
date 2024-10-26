grid = [input().strip() for _ in range(8)]

empty_rows = sum(1 for row in grid if '#' not in row)

empty_columns = 0
for col in range(8):
    if all(grid[row][col] == '.' for row in range(8)):
        empty_columns += 1

ans = empty_columns*empty_rows

print(ans)
