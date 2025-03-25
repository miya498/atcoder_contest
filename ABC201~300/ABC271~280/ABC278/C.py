N, Q = map(int, input().split())

# フォロー関係を管理する隣接リスト
follow = set()

for _ in range(Q):
    t, a, b = map(int, input().split())

    if t == 1:
        follow.add((a,b))

    elif t == 2:
        follow.discard((a,b))

    elif t == 3:
        # ユーザー A と B が互いにフォローしているかチェック
        if (a,b) in follow and (b,a) in follow:
            print("Yes")
        else:
            print("No")