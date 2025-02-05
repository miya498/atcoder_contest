# Python `collections` モジュールの概要

Python の `collections` モジュールは、標準のデータ型 (`dict`, `list`, `tuple` など) を拡張した、より強力で便利なデータ構造を提供します。

## **主なデータ構造**

### 1. `defaultdict`
キーが存在しない場合に、自動でデフォルト値を設定できる辞書。

### 2. `Counter`
リストや文字列の要素の出現回数を数えるための辞書。

### 3. `deque`
両端から高速に要素を追加・削除できるキュー（双方向キュー）。

### 4. `OrderedDict`
キーの順序を保持する辞書（Python 3.7 以降は `dict` でも順序保持）。

### 5. `namedtuple`
名前付きタプル。通常のタプルより可読性が向上。

### 6. `ChainMap`
複数の辞書を1つにまとめて管理できるデータ構造。

### 7. `UserDict`, `UserList`, `UserString`
`dict`, `list`, `str` を拡張したカスタマイズ可能なデータ構造。

---

## **`collections` を活用すべき場面**
| シナリオ | 適したデータ構造 |
|------|------|
| 頻度カウント | `Counter` |
| デフォルト値付き辞書 | `defaultdict` |
| 両端キュー処理 | `deque` |
| 順序付き辞書 | `OrderedDict` |
| 軽量なオブジェクト | `namedtuple` |
| 複数辞書の統合 | `ChainMap` |

---

この `README.md` では、`collections` の概要を説明しました。次に、各モジュールの使用方法を `.json` 形式で作成します。

