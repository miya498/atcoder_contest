
# Union-Find データ構造

Union-Find（Disjoint Set Union, DSU）は、以下の操作を効率的に行うためのデータ構造です：

1. **Union（統合）**: 2つの集合を統合します。
2. **Find（検索）**: 要素が属する集合の代表（ルート）を見つけます。

## 特徴

- 要素が同じ集合に属しているかを判定することができます。
- 集合の統合操作を高速に行うことができます。
- データをツリー構造で管理し、経路圧縮（Path Compression）やランク（Rank）を利用して効率化します。

## 主な用途

- グラフの連結成分を判定
- 最小全域木の構築（Kruskal法）
- 動的な集合管理

## 主な操作

### 1. Find（検索）
ある要素が属する集合の代表（ルート）を返します。経路圧縮を行うことで、ツリーの高さを減らし、後続の操作を効率化します。

### 2. Union（統合）
2つの集合を統合します。ランクやサイズを利用して、小さい方を大きい方にマージすることで、ツリーの高さを抑えます。

## 計算量

- Find: \\(O(\\alpha(n))\\)
- Union: \\(O(\\alpha(n))\\)

\\(\\alpha(n)\\) はアッカーマン関数の逆関数であり、実用上ほぼ定数と考えられます。

---

## テンプレートコード

以下は Python での Union-Find のテンプレートコードです。コメント付きで詳しく説明しています：

```python
class UnionFind:
    def __init__(self, n):
        # 各要素の親ノードを記録する配列
        self.parent = list(range(n))  # 初期状態では各要素が自分自身を親とする
        # 各集合のランク（木の高さ）を記録する配列
        self.rank = [1] * n  # 初期ランクはすべて1

    def find(self, x):
        # 要素 x の親を再帰的に探す
        if self.parent[x] != x:
            # 経路圧縮: ルートノードを直接親とする
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # x と y を含む集合を統合する
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            # ランクの小さい方を大きい方に統合する
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                # ランクが同じ場合はどちらかを親にしてランクを1増やす
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def is_same(self, x, y):
        # x と y が同じ集合に属するか判定する
        return self.find(x) == self.find(y)
