N = int(input())
ans = 0
for i in range(1,6):
    num = 1000**i
    if N >= num:
        ans += N-num+1
print(ans)