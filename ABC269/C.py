def generate_subsets(N):
    # ビットが1の位置を取得
    positions = [i for i in range(N.bit_length()) if (N >> i) & 1]
    
    # 部分集合を生成
    subsets = []
    for mask in range(1 << len(positions)):  # 2^len(positions) 個の部分集合
        x = 0
        for j in range(len(positions)):
            if (mask >> j) & 1:  # 部分集合に含まれる場合
                x |= (1 << positions[j])
        subsets.append(x)
    
    # 結果を昇順に出力
    subsets.sort()
    return subsets

# 入力と出力
N = int(input())
result = generate_subsets(N)
for x in result:
    print(x)