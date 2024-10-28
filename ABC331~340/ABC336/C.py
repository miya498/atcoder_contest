N = int(input()) - 1
five = []

while True:
    d = N % 5
    N = N // 5
    five.insert(0, d)  # dは整数
    if N < 5:  # Nが5未満になったら、最後に残りを挿入して終了
        five.insert(0, N)
        break

# リストの要素を文字列に変換して結合し、整数に変換
ans = int("".join(map(str, five)))

# 結果を2倍して表示
print(ans * 2)