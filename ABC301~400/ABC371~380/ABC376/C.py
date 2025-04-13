def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 配列をソート
    a.sort()
    
    ok = 1 << 30  # 大きい初期値
    ng = 0  # 小さい初期値

    # 条件をチェックする関数
    def f(x):
        nb = b[:]  # bのコピーを作成
        nb.append(x)  # xを追加
        nb.sort()  # ソート
        for i in range(n):
            if a[i] > nb[i]:  # aの要素がnbの要素より大きい場合
                return False
        return True

    # okの値でfをチェック
    if not f(ok):
        print(-1)
        return

    # 二分探索
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid

    print(ok)

# メイン関数を呼び出す
if __name__ == "__main__":
    main()
