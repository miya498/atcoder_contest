# 動的計画法についての解説

動的計画法（Dynamic Programming）は、問題を部分問題に分割し、重複する計算を避けながら解を求める手法です。通常、再帰的に解決できる問題を効率的に解くために使用され、最適化問題に頻繁に利用されます。ここでは、代表的な動的計画法のアルゴリズムについて解説します。

---

## 動的計画法の基本概念

動的計画法では、問題を解決する際に次の二つの特徴が求められます：

1. **重複部分問題（Overlapping Subproblems）**  
   問題を再帰的に分割すると、同じ部分問題が繰り返し登場する場合です。DPではこれを利用して、一度計算した結果を再利用します。

2. **最適部分構造（Optimal Substructure）**  
   問題の最適解が、その部分問題の最適解を利用して構成できる場合です。DPはこの性質を活かし、サブプロブレムの解を組み合わせて全体の解を構成します。

---

## ナップサック問題 (Knapsack Problem)

ナップサック問題は、与えられた重量制限の中で、アイテムの価値を最大化する組み合わせを求める問題です。DPでは、次のように部分問題を構成して解決します：

- **入力**：`n`個のアイテム、各アイテムの重さと価値、およびナップサックの最大重量`W`
- **出力**：最大の総価値

### アプローチ
- 配列`dp[i][w]`を用意し、`i`番目までのアイテムで重さ`w`以下で達成できる最大価値を保持します。
- **計算量**：`O(n * W)`

---

## フィボナッチ数列 (Fibonacci Sequence)

フィボナッチ数列は、DPで効率的に計算できる典型例です。基本的には再帰で解けますが、計算の重複が多いため、DPで最適化します。

- **定義**：`F(n) = F(n-1) + F(n-2)`で`n > 1`
- **計算量**：`O(n)`

### メモ化とボトムアップアプローチ
- **メモ化**：再帰での計算結果を保存し、再利用します。
- **ボトムアップ**：最初から順に`F(0)`から計算し、`F(n)`に到達する方法です。

---

## 最長共通部分列 (Longest Common Subsequence, LCS)

最長共通部分列（LCS）問題は、2つのシーケンス（文字列）間で共通部分の最長のものを見つける問題です。たとえば、`"ABCBDAB"`と`"BDCAB"`のLCSは`"BCAB"`です。

- **入力**：2つのシーケンス`X`と`Y`
- **出力**：共通部分の最大長

### アプローチ
- 配列`dp[i][j]`を用意し、`X[0..i]`と`Y[0..j]`のLCS長を格納します。
- **計算量**：`O(m * n)`（`m`と`n`はそれぞれのシーケンス長）

---

## 部分和問題 (Subset Sum Problem)

部分和問題は、与えられた集合の一部の要素を足し合わせて特定の値を作れるかどうかを判定する問題です。

- **入力**：整数のリスト`arr`と目標値`sum`
- **出力**：部分集合の和が`sum`となるかどうか

### アプローチ
- 配列`dp[i][j]`を用意し、`i`番目までの要素で和`j`が作れるかどうかを判定します。
- **計算量**：`O(n * sum)`

---

## まとめ

| アルゴリズム             | 入力                       | 出力               | 計算量            |
|--------------------------|----------------------------|--------------------|-------------------|
| ナップサック問題         | アイテムの価値と重さ、容量 | 最大の価値の組み合わせ | `O(n * W)`    |
| フィボナッチ数列         | 数列の長さ                 | 数列の`n`番目の値 | `O(n)`          |
| 最長共通部分列           | 2つのシーケンス            | 最大共通部分の長さ | `O(m * n)`     |
| 部分和問題               | 整数のリストと目標値       | 和が目標に達するか | `O(n * sum)`   |

---

### 動的計画法のメリットとデメリット

**メリット**
- 重複する計算を避けることで、再帰より効率的に問題を解決できます。
- 複雑な問題も、小さな部分問題に分解して考えられます。

**デメリット**
- 配列を用いるため、メモリ使用量が増加する可能性があります。
- 問題によっては、DPのアプローチがわかりにくいことがあります。