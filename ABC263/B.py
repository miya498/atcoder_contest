# 入力の受け取り
N = int(input())
P = list(map(int, input().split()))  # P[0] = 親の情報 (2 から N までの親)

# 人 N から親をたどる
current = N  # 現在の人の番号
generation_count = 0  # 世代をカウント

while current != 1:  # 人 1 に到達するまで
    current = P[current - 2]  # 親をたどる (P[0] は人 2 の親)
    generation_count += 1

print(generation_count)