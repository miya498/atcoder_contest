# 入力の取得
N, Q = map(int, input().split())

# 鳩がいる巣の情報 (pigeon[i] は鳩 i がいる巣の論理番号)
pigeon = list(range(N + 1))

# 物理的な巣から論理巣への対応付け
phys_to_log = list(range(N + 1))

# 論理巣から物理的な巣への対応付け
log_to_phys = list(range(N + 1))

# クエリの処理
for _ in range(Q):
    q = list(map(int, input().split()))
    
    if q[0] == 1:
        # 種類 1: 鳩 a を巣 b へ移動
        a, b = q[1], q[2]
        pigeon[a] = phys_to_log[b]  # 鳩 a を巣 b の論理番号へ移動

    elif q[0] == 2:
        # 種類 2: 巣 a と 巣 b の鳩を交換
        a, b = q[1], q[2]
        
        # 現在の巣 a と b の論理番号を取得
        log_a, log_b = phys_to_log[a], phys_to_log[b]
        
        # 巣の論理番号を入れ替える
        phys_to_log[a], phys_to_log[b] = log_b, log_a
        log_to_phys[log_a], log_to_phys[log_b] = b, a  # 論理番号に対応する物理巣番号も更新

    elif q[0] == 3:
        # 種類 3: 鳩 a がいる巣の番号を出力
        a = q[1]
        print(log_to_phys[pigeon[a]])  # 鳩 a のいる論理巣の物理巣番号を出力