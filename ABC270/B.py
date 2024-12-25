# 入力の受け取り
X,Y,Z=map(int,input().split())

# -1になるパターン
if 0<Y<X<Z or 0<Y<Z<X or X<Z<Y<0 or Z<X<Y<0:
    # -1を出力
    print(-1)
# 2|Z|+|X|になるパターン
elif X<Y<0<Z or Z<0<Y<X:
    # 2|Z|+|X|を出力
    print(2*abs(Z)+abs(X))
# それ以外
else:
    # |X|を出力
    print(abs(X))