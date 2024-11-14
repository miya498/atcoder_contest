# クエリ数の読み込み
Q = int(input())

# 植物の初期化
plants = []
total_growth = 0
result = []

# クエリ処理
for _ in range(Q):
    query = input().split()
    query_type = int(query[0])
    
    if query_type == 1:
        plants.append(0)
    
    elif query_type == 2:
        T = int(query[1])
        for i in range(len(plants)):
            plants[i] += T
    
    elif query_type == 3:

        H = int(query[1])
        count = 0
        
        remaining_plants = []
        for height in plants:
            if height >= H:
                count += 1
            else:
                remaining_plants.append(height)
        result.append(count)
        plants = remaining_plants

# 結果の出力
print("\n".join(map(str, result)))