N = int(input())
water = 0
time = 0

for _ in range(N):
    t, v = map(int, input().split())
    water -= (t - time)
    if water < 0:
        water = 0
    water += v
    time = t

print(water)