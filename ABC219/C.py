X = input()
N = int(input())
S = [input() for _ in range(N)]

# X に基づく順序を辞書として格納
order = {ch: i for i, ch in enumerate(X)}

# ソート用のキーを作成
def transform(s):
    return [order[ch] for ch in s]  # 各文字を数値に変換

# 数値リストをキーにしてソート
S_sorted = sorted(S, key=transform)

# 出力
print("\n".join(S_sorted))
