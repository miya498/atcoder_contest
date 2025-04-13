N = int(input())
S = list(input())

alph = [0] * 26

i = 0
while i < N:
    j = i
    while j < N and S[i] == S[j]:
        j += 1
    num = ord(S[i]) - ord("a")
    alph[num] = max(alph[num], j - i)  # 同じ文字の連続長を記録
    i = j  # i を次の異なる文字に進める

# 合計を求める
ans = sum(alph)

# 結果を出力
if N != 1:
    print(ans)
else:
    print(1)
