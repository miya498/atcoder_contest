# 商品数 n、機能の種類数 m を読み込み
n, m = map(int, input().split())
p = []  # 各商品の価格を格納するリスト
f = []  # 各商品の機能リストを格納するリスト

# 各商品の情報を入力し、価格と機能をそれぞれのリストに分けて格納
for i in range(n):
    product = list(map(int, input().split()))
    p.append(product[0])       # 価格を p に追加
    f.append(product[2:])       # 機能を f に追加（product[1] は機能数なのでスキップ）

# 上位互換を見つけたかを判定するためのフラグ
result = False

# 2重ループで全ての組み合わせを比較
for i in range(n):
    for j in range(n):
        # 同一商品でないこと、かつ i の価格が j の価格以上であることが条件
        if i == j or p[i] < p[j]:
            continue

        # i の機能がすべて j の機能に含まれているかをチェック
        temp = True
        for e in f[i]:           # i の機能リストの各機能を e に取り出す
            if e not in f[j]:     # i の機能が j に含まれていない場合
                temp = False      # 上位互換の条件を満たさないので False に設定
                break             # これ以上チェックせず次の組み合わせへ

        # すべての条件を満たす場合に上位互換を検出
        if temp:
            # i の価格が j の価格より高い、もしくは i の機能数が j より少ない場合に上位互換
            if p[i] > p[j] or len(f[i]) < len(f[j]):
                result = True     # 上位互換が存在することを示すフラグを True に設定
                break             # 一つでも見つかれば終了
    if result:
        break                     # 外側のループも終了

# 結果の出力
print("Yes" if result else "No")