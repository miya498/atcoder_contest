N = int(input())
S = [input() for _ in range(N)]
S.sort(key=len)
ans = ""
for s in S:
    ans += s
print(ans)