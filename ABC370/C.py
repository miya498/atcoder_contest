S = list(input())
T = list(input())

ans = 0

# 異なる文字の数を数え、S > T になる箇所のカウント
for i in range(len(S)):
    if S[i] != T[i]:
        ans += 1

print(ans)

# まず、S[i] > T[i] の箇所をT[i]に書き換える
for i in range(len(S)):
    if S[i] > T[i] :
        S[i] = T[i]
        print("".join(S))

# 残りの異なる部分をTに書き換える
for i in range(len(S)):
    if S[len(S)-i-1] != T[len(S)-i-1]:
        S[len(S)-i-1] = T[len(S)-i-1]
        print("".join(S))