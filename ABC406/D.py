H, W, N = map(int, input().split())
row_garb = [[] for _ in range(H+1)]
col_garb = [[] for _ in range(W+1)]
row_count = [0] * (H+1)
col_count = [0] * (W+1)

for _ in range(N):
    x, y = map(int, input().split())
    row_garb[x].append(y)
    col_garb[y].append(x)
    row_count[x] += 1
    col_count[y] += 1

row_removed = [False] * (H+1)
col_removed = [False] * (W+1)

Q = int(input())
for _ in range(Q):
    t, v = map(int, input().split())
    if t == 1:
        # Row query
        if row_removed[v]:
            print(0)
            continue
        ans = row_count[v]
        print(ans)
        row_removed[v] = True
        row_count[v] = 0
        # Remove those garbages from their columns
        for y in row_garb[v]:
            if not col_removed[y]:
                col_count[y] -= 1
    else:
        # Column query
        if col_removed[v]:
            print(0)
            continue
        ans = col_count[v]
        print(ans)
        col_removed[v] = True
        col_count[v] = 0
        # Remove those garbages from their rows
        for x in col_garb[v]:
            if not row_removed[x]:
                row_count[x] -= 1