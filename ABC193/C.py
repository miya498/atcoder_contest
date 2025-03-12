N = int(input())
power_set = set()

# a^2 <= N となる a について探索（a は 2 以上）
a = 2
while a * a <= N:
    p = a * a  # 最小の b=2 のとき
    while p <= N:
        power_set.add(p)
        p *= a  # 次の指数
    a += 1

# N から a^b として表せる数の個数を引く
print(N - len(power_set))