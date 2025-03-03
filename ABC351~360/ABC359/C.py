Sx, Sy = map(int, input().split())
Tx, Ty = map(int, input().split())

# タイルの左側に寄せておく
if (Sx + Sy) % 2 == 1:
    Sx -= 1
if (Tx + Ty) % 2 == 1:
    Tx -= 1

# 答えは (|Sy - Ty| + max(|Sx - Tx|, |Sy - Ty|)) / 2
Dx = abs(Sx - Tx)
Dy = abs(Sy - Ty)

print((Dy + max(Dx, Dy)) // 2)
