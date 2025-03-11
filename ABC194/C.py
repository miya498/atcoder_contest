N = int(input())
A = list(map(int,input().split()))

cnt = [0 for _ in range(401)]

for a in A:
    cnt[a+200] += 1

ans = 0

for i in range(401):
    for j in range(401):
        ans += cnt[i]*cnt[j]*(i-j)**2

print(ans//2)