from collections import defaultdict

N, M = map(int, input().split())
lines = defaultdict(int)
for _ in range(M):
    a, b = map(int, input().split())
    lines[(a+b)%N] += 1
ans = M*(M-1)//2
non_cross = 0
for cnt in lines.values():
    non_cross += cnt*(cnt-1)//2
print(ans-non_cross)
