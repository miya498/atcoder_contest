# 2次元配列内の'#'の数を返す関数
def black_cnt(lis):
    cnt = 0
    for row in lis:
        cnt += row.count('#')
    return cnt


Ha, Wa = map(int, input().split())
A = [input() for _ in range(Ha)]
black_A = black_cnt(A)
Hb, Wb = map(int, input().split())
B = [input() for _ in range(Hb)]
black_B = black_cnt(B)
Hx, Wx = map(int, input().split())
X = [input() for _ in range(Hx)]


def is_ok(ia, ja, ib, jb):
    """
    ・シートAとシートYについて
    シートYが(Ha,Wa)～(Ha+Hx-1,Wa+Wx-1)の位置で、
    シートAが(ia,ja)～(ia+Ha-1,ja+Wa-1)の位置のとき

    ・シートBとシートYについて
    シートYが(Hb,Wb)～(Hb+Hx-1,Wb+Wx-1)の位置で、
    シートBが(ib,jb)～(ib+Hb-1,jb+Wb-1)の位置のとき
    """
    Y = [['.'] * Wx for _ in range(Hx)]
    cnt_a, cnt_b = 0, 0

    # シートYの各点が塗れるかどうかを調べる。
    for i in range(Hx):
        for j in range(Wx):
            di, dj = Ha + i - ia, Wa + j - ja
            if 0 <= di < Ha and 0 <= dj < Wa:
                if A[di][dj] == '#':
                    Y[i][j] = '#'
                    cnt_a += 1
            di, dj = Hb + i - ib, Wb + j - jb
            if 0 <= di < Hb and 0 <= dj < Wb:
                if B[di][dj] == '#':
                    Y[i][j] = '#'
                    cnt_b += 1
    
    # シートAについて、シートAにある'#'がすべて使われていなかったらアウト
    # シートBについてもおなじ
    if cnt_a != black_A or cnt_b != black_B:
        return False
    
    # シートXとシートYの一致判定
    for i in range(Hx):
        for j in range(Wx):
            if X[i][j] != Y[i][j]:
                return False
    return True


# シートAで、最初(0,0)だった点が(ia,ja)の点に移動している状態
for ia in range(Ha + Hx):
    for ja in range(Wa + Wx):
        # シートBで、最初(0,0)だった点が(ib,jb)の点に移動している状態
        for ib in range(Hb + Hx):
            for jb in range(Wb + Wx):
                if is_ok(ia, ja, ib, jb):
                    print("Yes")
                    exit()
print("No")