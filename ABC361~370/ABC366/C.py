from collections import Counter

# クエリの数を入力
Q = int(input())

# カウンタでボールの種類と個数を管理
bag = Counter()

# クエリを順次処理
for _ in range(Q):
    query = input().split()
    
    if query[0] == '1':
        # ボールを追加する（ボールの種類xの数を増やす）
        x = int(query[1])
        bag[x] += 1

    elif query[0] == '2':
        # ボールを1つ取り出す（ボールの種類xの数を減らす）
        x = int(query[1])
        bag[x] -= 1
        if bag[x] == 0:
            del bag[x]  # 数が0になったら袋から削除

    elif query[0] == '3':
        # 種類の数を出力する
        print(len(bag))