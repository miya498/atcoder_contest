N = int(input())
A = list(map(int,input().split()))

cnt = [0 for _ in range(3*N)]

ans = []

for i in A:
    cnt[i] += 1
    if cnt[i] == 2:
        ans.append(i)

print(*ans)