from collections import Counter
N = int(input())
S = [str(sorted(list(input()))) for _ in range(N)]

ans = 0
cnt = Counter(S)
for i in cnt.values():
    ans += i*(i-1)//2
print(ans)

