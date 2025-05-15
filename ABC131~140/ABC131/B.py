def solve():
    import sys
    input = sys.stdin.readline

    N, L = map(int, input().split())
    # 全てのリンゴの味の総和
    S = N*L + N*(N-1)//2

    # 味の並びは [L, L+1, ..., L+N-1]
    # この中から 0 に最も近い値を選ぶ
    # インデックス i (0-based) での味は L + i
    # i_min = min(max(-L, 0), N) が最小の i で L+i >= 0 となるように clamped
    i_min = -L
    if i_min < 0:
        i_min = 0
    elif i_min > N:
        i_min = N

    candidates = []
    if 0 < i_min <= N:
        candidates.append(L + (i_min - 1))
    if 0 <= i_min < N:
        candidates.append(L + i_min)

    # 最も絶対値が小さい味を選ぶ
    eat = min(candidates, key=lambda x: abs(x))

    # 残った N-1 個のリンゴで作るアップルパイの味
    print(S - eat)


if __name__ == "__main__":
    solve()
