S = input().strip()
T = input().strip()

min_len = min(len(S), len(T))  # 2つの文字列のうち短い方の長さ
diff_pos = 0  # 異なる文字が出現する位置を保持

# 先頭から文字を比較して異なる文字があれば位置を記録
for i in range(min_len):
    if S[i] != T[i]:
        diff_pos = i + 1  # 1から数えるため、インデックス+1
        break

# もし等しい部分が全て同じで長さが違う場合
if diff_pos == 0 and len(S) != len(T):
    diff_pos = min_len + 1  # 短い方の次の位置を出力

# もし等しい場合、diff_pos は 0 のままなので、それを使って出力
if diff_pos == 0 and len(S) == len(T):
    print(0)
else:
    print(diff_pos)