N = int(input())  # 技の数
TKA = [list(map(int, input().split())) for _ in range(N)]  # 技のデータを取得

# スタック（技を習得する順番を管理）
stack = [N-1]  # 技 N を習得するために必要な技を管理（0-indexed）
visited = [False] * N  # すでに習得した技を記録
visited[N-1] = True  # 技 N は最初に学ぶので True にする

total_time = 0  # 総修練時間

# 深さ優先探索（DFS）で必要な技を探索
while stack:
    current_skill = stack.pop()  # 現在習得しようとしている技
    skill_info = TKA[current_skill]  # 技の情報を取得
    total_time += skill_info[0]  # 習得時間を加算

    # もし前提技がないなら次へ
    if skill_info[1] == 0:
        continue

    # 前提技があるなら、それを習得する
    for i in range(skill_info[1]):
        prerequisite = skill_info[i+2] - 1  # 前提技のインデックス
        if not visited[prerequisite]:  # まだ習得していない場合
            visited[prerequisite] = True  # 習得済みにする
            stack.append(prerequisite)  # 習得すべき技として追加

# 最終的な習得時間を出力
print(total_time)