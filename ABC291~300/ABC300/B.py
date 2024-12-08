H, W = map(int, input().split())

# グリッドAとBの読み込み
A = [input() for _ in range(H)]
B = [input() for _ in range(H)]

# シフトを適用してBと一致するか確認
def is_match(A, B, s, t):
    for i in range(H):
        for j in range(W):
            # 縦方向s回、横方向t回シフト後の位置と一致するか
            if A[(i - s) % H][(j - t) % W] != B[i][j]:
                return False
    return True

# 全てのs, tの組み合わせを試す
for s in range(H):
    for t in range(W):
        if is_match(A, B, s, t):
            print("Yes")
            exit()

print("No")