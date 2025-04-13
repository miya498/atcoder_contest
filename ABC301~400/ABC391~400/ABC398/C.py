from collections import Counter
N = int(input())
A = list(map(int,input().split()))

cnt = Counter(A)

ans = -1
max_val = -1
for i,a in enumerate(A):
    if cnt[a] == 1:
        if a > max_val:
            max_val = a
            ans = i+1

if ans == -1:
    print(-1)
else:
    print(ans)