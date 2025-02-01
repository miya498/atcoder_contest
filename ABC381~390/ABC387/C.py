# 標準入力から L と R を取得
L, R = map(int, input().split())

# 桁DPを利用してヘビ数の個数を計算する関数
# pos       : 現在見ている桁の位置
# tight     : 現在の数が制限されているかどうか（制限ありなら1、なしなら0）
# first_digit : 先頭の非ゼロ桁の値
# nonzero   : 非ゼロの桁がすでに出ているか（出ていれば1、出ていなければ0）
# digits    : 数字を桁ごとに分割したリスト
def digit_dp(pos, tight, first_digit, nonzero, digits):
    # すべての桁を見終わった場合
    if pos == len(digits):
        # 非ゼロの数字が1つでもあればヘビ数としてカウント
        return 1 if nonzero else 0

    # メモ化された結果があれば再利用（DPキャッシュ）
    if dp[pos][tight][first_digit][nonzero] != -1:
        return dp[pos][tight][first_digit][nonzero]

    # 現在の桁の上限を設定（tightが1の場合、現在の桁の数字まで）
    limit = digits[pos] if tight else 9
    res = 0  # 現在の状態でのヘビ数の個数を格納

    # 現在の桁に入る数字 d を0から limit までループ
    for d in range(0, limit + 1):
        # 新しいtightを設定（現在の桁が上限に等しい場合のみtightを維持）
        new_tight = tight and (d == limit)

        # すでに非ゼロの桁を見ている場合
        if nonzero:
            # 現在の桁 d が先頭の桁より大きい場合はスキップ（ヘビ数の条件を満たさない）
            if d >= first_digit:
                continue
        else:
            # まだ非ゼロの桁を見ていない場合、先頭の非ゼロ桁を更新
            first_digit = d

        # 再帰的に次の桁の状態を計算
        res += digit_dp(pos + 1, new_tight, first_digit, nonzero or d > 0, digits)

    # 現在の状態をメモ化（DPキャッシュに保存）
    dp[pos][tight][first_digit][nonzero] = res
    return res


# 範囲 [L, R] のヘビ数の個数を計算する関数
def count_heavy_numbers(L, R):
    # solve(n) は 0 から n までのヘビ数の個数を計算
    def solve(n):
        global dp
        # 数字 n を桁ごとのリストに変換
        digits = list(map(int, str(n)))
        # DP配列の初期化（4次元配列）
        dp = [[[[-1] * 2 for _ in range(10)] for _ in range(2)] for _ in range(len(digits) + 1)]
        # 桁DPで計算を開始
        return digit_dp(0, 1, 0, 0, digits)

    # [L, R] のヘビ数の個数は solve(R) - solve(L-1)
    return solve(R) - solve(L - 1)


# ヘビ数の個数を計算して出力
ans = count_heavy_numbers(L, R)
print(ans)