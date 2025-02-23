N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

# すぬけ君の宝石をもらう時刻を記録
ans = T[:]  # 初期値はTで初期化

# 2N 回繰り返して更新（最低2周する）
for i in range(2 * N):
    next_i = (i + 1) % N  # 次のすぬけ君（円環構造）
    ans[next_i] = min(ans[next_i], ans[i % N] + S[i % N])  # 早い方を選ぶ

for a in ans:
    print(a)