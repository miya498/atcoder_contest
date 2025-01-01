import pandas as pd
import os

# Excelファイルのパス
file_path = "atcoder_problems_by_contest.xlsx"

# 入力データ
contest_name = input("コンテスト名を入力してください (例: ABC001): ").strip()
problem_name = input("問題名を入力してください (例: A, B, C, ...): ").strip()
problem_type = input("解法タイプを入力してください (例: bit全探索, 動的計画法など): ").strip()

# 解けたかどうかを入力
print("解けたかどうかを番号で入力してください (1: ○, 2: △, 3: ×)")
while True:
    try:
        result_input = int(input("評価 (1, 2, 3): "))
        if result_input in [1, 2, 3]:
            break
        else:
            print("1, 2, 3 のいずれかを入力してください。")
    except ValueError:
        print("数字を入力してください。")

# 評価を文字に変換
result_map = {1: "○", 2: "△", 3: "×"}
result = f"{problem_type} ({result_map[result_input]})"  # タイプと評価をまとめる

# Excelファイルの読み込みまたは新規作成
if os.path.exists(file_path):
    df = pd.read_excel(file_path, index_col=0)
else:
    # 空のデータフレームを作成（新規作成時の列を定義）
    df = pd.DataFrame(columns=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])

# コンテスト名が既に存在するか確認
if contest_name not in df.index:
    df.loc[contest_name] = pd.Series(dtype=str)

# 問題名を列に追加または更新
df.at[contest_name, problem_name] = result

# コンテスト名を降順にソート
df = df.sort_index(
    ascending=False,
    key=lambda x: x.str.extract(r'(\d+)$').iloc[:, 0].astype(int)
)

# Excelに書き込む
df.to_excel(file_path)

print(f"問題情報が追記されました: {file_path}")