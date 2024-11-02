from collections import defaultdict

# 入力の受け取り
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 累積和の剰余の初期化
prefix_sum_mod = 0
mod_count = defaultdict(int)
mod_count[0] = 1  # 初期状態として累積和が0の剰余を1つ持っているとする

total_sum_mod = 0

# 累積和を計算しながら剰余をカウント
for num in A:
    # 剰余が負にならないようにするための調整
    prefix_sum_mod = (prefix_sum_mod + M) % M


    # 現在の累積和の剰余が出現している回数を結果に加算
    total_sum_mod += mod_count[prefix_sum_mod]

    # 現在の剰余をカウント
    mod_count[prefix_sum_mod] += 1

# 結果の出力
print(total_sum_mod)