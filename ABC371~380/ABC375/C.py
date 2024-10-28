def move(x, y, cnt):
    if cnt % 4 == 0:
        return x, y
    elif cnt % 4 == 1:
        return n - y - 1, x
    elif cnt % 4 == 2:
        return n - x - 1, n - y - 1
    else:
        return y, n - x - 1

n = int(input())
a = [list(input()) for _ in range(n)]
ans = [["."] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        x, y = move(i, j, min(i + 1, j + 1, n - i, n - j))
        ans[i][j] = a[x][y]

for a_i in ans:
    print("".join(a_i))