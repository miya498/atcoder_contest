def generate_carpet(N):
    # 基本ケース: Nが0の時は黒いマス（#）のみを返す
    if N == 0:
        return ['#']

    # レベル(N-1)のカーペットをまず生成
    smaller_carpet = generate_carpet(N - 1)
    size = len(smaller_carpet)
    new_size = size * 3

    # レベルNのカーペット用の新しいグリッドを初期化
    carpet = [[' '] * new_size for _ in range(new_size)]

    # レベル(N-1)のカーペットを8つのブロックに配置
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                # 中央のブロックは白いマス('.')
                for x in range(size):
                    for y in range(size):
                        carpet[size * i + x][size * j + y] = '.'
            else:
                # 他のブロックにはレベル(N-1)のカーペットを配置
                for x in range(size):
                    for y in range(size):
                        carpet[size * i + x][size * j + y] = smaller_carpet[x][y]

    # カーペットをリストで返す
    return [''.join(row) for row in carpet]

# カーペットのレベルNを入力
N = int(input())

# レベルNのカーペットを生成して出力
carpet = generate_carpet(N)
for row in carpet:
    print(row)