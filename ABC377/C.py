N, M = map(int, input().split())
knights = [tuple(map(int, input().split())) for _ in range(M)]

# 騎馬の攻撃範囲の移動パターン
moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

# 攻撃範囲を記録するセット
attackable_positions = set()

# 各騎馬の攻撃範囲を追加
for (a, b) in knights:
    for da, db in moves:
        na, nb = a + da , b + db 
        # 範囲内チェック
        if 1 <= na <= N and 1 <= nb <= N:
            attackable_positions.add((na, nb))
        attackable_positions.add((a,b))


# 結果出力
non_attackable_count = N * N - len(attackable_positions)
print(non_attackable_count)
