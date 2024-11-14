N = int(input())

flavor = [[] for _ in range(N)]

for _ in range(N):
    f, s = map(int, input().split())
    flavor[f-1].append(s)

for i in range(N):
    flavor[i].sort(reverse=True)

same_select = 0

for i in range(N):
    if len(flavor[i]) >= 2:
        same_select = max(same_select,flavor[i][0]+flavor[i][1]//2)

diff_select = 0

top = []
for i in range(N):
    if len(flavor[i]) >= 1:
        top.append(flavor[i][0])
top.sort(reverse=True)
diff_select = max(diff_select,sum(top[:2]))

print(max(diff_select,same_select))