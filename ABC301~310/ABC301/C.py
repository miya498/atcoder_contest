# 入力
S = input()
T = input()

# @ のカードで置き換え可能な文字
valid_chars = set("atcoder")

# カードの出現回数をカウント
count_s = {}
count_t = {}

for char in S:
    count_s[char] = count_s.get(char, 0) + 1

for char in T:
    count_t[char] = count_t.get(char, 0) + 1

# 判定
for char in set(S + T):
    if char in valid_chars:
        continue
    if char != '@' and count_s.get(char, 0) != count_t.get(char, 0):
        print("No")
        exit()

# @ を利用して調整
remaining_s = count_s.get('@', 0)
remaining_t = count_t.get('@', 0)

for char in valid_chars:
    diff_s = max(0, count_t.get(char, 0) - count_s.get(char, 0))
    diff_t = max(0, count_s.get(char, 0) - count_t.get(char, 0))
    remaining_s -= diff_s
    remaining_t -= diff_t

if remaining_s >= 0 and remaining_t >= 0:
    print("Yes")
else:
    print("No")