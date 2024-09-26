S = input("文字列を入力してください: ")
N = len(S)
ans = 0

# ビット全探索の範囲を 2**(N-1) に修正
for bit in range(2 ** (N - 1)):
    s = S[0]
    total = 0
    print(f"bit: {bin(bit)[2:].zfill(N-1)}", end=" => ")
    
    # 0 から N-2 までを処理 (S[N-1] はループ外で処理する)
    for i in range(N - 1):
        # 現在のビットが 1 ならば、現在の数値を合計に加える
        #1 << i 00001をi左シフトにずらす
        #例:1 << 2 =>100(2進数)
        if bit & (1 << i):
            total += int(s)
            print(f"{s} + ", end="")
            s = ""
        # 次の文字を追加する
        s += S[i + 1]
    
    # 最後の数値を合計に加える
    total += int(s)
    print(f"{s} = {total}")
    
    # 合計を更新
    ans += total

print(f"\n最終合計: {ans}")