# 定数の定義
MOD = 10**9 + 7

# 入力の読み込み
N = int(input())
S = input()

# 総和を格納する変数
total_sum = 0
current_sum = 0
multiplier = 1  # 各桁の10進法での重みを管理する

for i in range(N - 1, -1, -1):
    # 各桁の寄与の計算
    digit = int(S[i])
    current_sum = (current_sum + digit * multiplier * (i + 1)) % MOD
    total_sum = (total_sum + current_sum) % MOD
    
    # 次の桁への multiplier の更新
    multiplier = (multiplier * 10 + 1) % MOD

print(total_sum)