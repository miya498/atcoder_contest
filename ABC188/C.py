n = int(input())
a = list(map(int, input().split()))

total = 1 << n  # 2^n 人の選手
# remaining には、まだ負けていない選手の 0-indexed 番号を格納（初期状態は全選手）
remaining = list(range(total))

# トーナメントをシミュレーションする
for i in range(1, n + 1):
    next_remaining = []
    # ペアごとに対戦（remaining のサイズは必ず偶数となる）
    for j in range(0, len(remaining), 2):
        # レートが高いほうが勝つ
        if a[remaining[j]] > a[remaining[j + 1]]:
            next_remaining.append(remaining[j])
        else:
            next_remaining.append(remaining[j + 1])
    # 決勝ラウンドなら、直前の remaining（2 人）から準優勝者を求める
    if i == n:
        champion = next_remaining[0]  # 決勝で勝った選手
        # 直前の remaining は対戦前の 2 人のリスト
        if remaining[0] == champion:
            runner_up = remaining[1]
        else:
            runner_up = remaining[0]
        # 出力は 1-indexed なので +1
        print(runner_up + 1)
        break
    # 次ラウンドへ進む
    remaining = next_remaining