def check_totu(x1, y1, x2, y2, x3, y3):
    # ベクトル (x2 - x1, y2 - y1) と (x3 - x2, y3 - y2) の外積を計算
    # 外積が正であれば反時計回り、負であれば時計回り
    cross_product = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
    return cross_product > 0

A_x, A_y = map(int, input().split())
B_x, B_y = map(int, input().split())
C_x, C_y = map(int, input().split())
D_x, D_y = map(int, input().split())

# 各辺の向きがすべて反時計回りなら四角形は凸
if (check_totu(A_x, A_y, B_x, B_y, C_x, C_y) and
    check_totu(B_x, B_y, C_x, C_y, D_x, D_y) and
    check_totu(C_x, C_y, D_x, D_y, A_x, A_y) and
    check_totu(D_x, D_y, A_x, A_y, B_x, B_y)):
    print("Yes")
else:
    print("No")