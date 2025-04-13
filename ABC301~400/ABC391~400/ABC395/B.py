N = int(input())

grid = [['.' for _ in range(N)] for _ in range(N)]

for i in range(1,N+1):
    j = N + 1 - i
    if i <= j:
        if i % 2 == 1:
            color = '#'
        else:
            color = "."
        for x in range(i - 1, j):
            for y in range(i - 1, j):
                grid[x][y] = color

for row in grid:
    print("".join(row))
