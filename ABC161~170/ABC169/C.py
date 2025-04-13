from decimal import Decimal, getcontext

# 十分な精度を設定（必要に応じて調整してください）
getcontext().prec = 100

A, B = map(Decimal, input().split())
print(int(A * B))