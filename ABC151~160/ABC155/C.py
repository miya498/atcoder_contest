from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

cnt = Counter(S)
max_v = max(cnt.values())

ans = []
for key,value in cnt.items():
    if value == max_v:
        ans.append(key)

ans.sort()

for i in range(len(ans)):
    print(ans[i])
