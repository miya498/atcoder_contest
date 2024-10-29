def is_one_char_replace(A, B):
    """文字列 A と B が1文字だけ異なるかを判定する関数"""
    diff_count = sum(1 for a, b in zip(A, B) if a != b)
    return diff_count <= 1

def is_one_char_insert_or_delete(A, B):
    """文字列 A に1文字挿入または削除することで B と一致するかを判定する関数"""
    # A を短い方、B を長い方に固定
    if len(A) > len(B):
        A, B = B, A

    # 短い方 A のインデックス i、長い方 B のインデックス j
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] != B[j]:
            # 一致しない場合は B 側だけインデックスを進め、後の文字が一致するか確認
            j += 1
            if i != j - 1:  # 2つ目の不一致があった場合
                return False
        else:
            i += 1
            j += 1
    return True

# 入力の受け取り
N, T = input().split()
N = int(N)
matching_indices = []

# 各文字列 S に対する比較
for idx in range(1, N + 1):
    S = input()
    if len(S) == len(T) and is_one_char_replace(S, T):
        # S と T の長さが同じで、1文字だけ異なる場合
        matching_indices.append(idx)
    elif abs(len(S) - len(T)) == 1 and is_one_char_insert_or_delete(S, T):
        # S と T の長さが1文字だけ異なり、1文字の挿入または削除で一致する場合
        matching_indices.append(idx)

# 結果の出力
print(len(matching_indices))
print(*matching_indices)