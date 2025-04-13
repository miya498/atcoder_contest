N = int(input())
cnt = [0 for _ in range(24)]

for i in range(N):
    w, x = map(int, input().split())
    cnt[x] += w

ans = 0
for t in range(24):  
    sum = 0
    for i in range(9):
        sum += cnt[(t+i)%24]
    ans = max(ans, sum)  # 最大人数を更新

print(ans)  # 最大人数を出力