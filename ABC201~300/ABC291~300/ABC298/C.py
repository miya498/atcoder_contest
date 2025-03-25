from collections import defaultdict

# 入力の読み込み
N = int(input())
Q = int(input())
queries = [input().split() for _ in range(Q)]

# 箱ごとのカードリスト
boxes = defaultdict(list)
# カードの値ごとの箱番号リスト
card_to_boxes = defaultdict(set)

for query in queries:
    if query[0] == '1':  # クエリ形式: 1 i j
        i = int(query[1])  # 数
        j = int(query[2])  # 箱番号
        boxes[j].append(i)
        card_to_boxes[i].add(j)
    
    elif query[0] == '2':  # クエリ形式: 2 i
        i = int(query[1])  # 箱番号
        if i in boxes:
            print(*sorted(boxes[i]))
        else:
            print()  # 箱が空の場合

    elif query[0] == '3':  # クエリ形式: 3 i
        i = int(query[1])  # 数
        if i in card_to_boxes:
            print(*sorted(card_to_boxes[i]))
        else:
            print()  # 数が書かれたカードが存在しない場合
