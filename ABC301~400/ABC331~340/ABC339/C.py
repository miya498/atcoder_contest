N = int(input())
A = list(map(int, input().split()))

current_passengers = 0
min_passengers = 0

# 累積和の中で最も低い値を見つける
for i in range(N):
    current_passengers += A[i]
    if current_passengers < 0:
        if -current_passengers > min_passengers:
            min_passengers = -current_passengers

ans = min_passengers

for i in range(N):
    ans += A[i]

# 最低限の乗客数を求める（0未満にならないようにする）
print(ans)