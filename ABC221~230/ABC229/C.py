N,W = map(int,input().split())
cheese = []
total = 0
for _ in range(N):
    a,b = map(int,input().split())
    cheese.append((a,b))
    total += b
cheese.sort(reverse=True)
w = 0
i = 0
ans = 0
while w < W and w < total:
    if w+cheese[i][1] < W:
        ans += cheese[i][0]*cheese[i][1]
        w += cheese[i][1]
        i += 1
    else:
        ans += cheese[i][0]*(W-w)
        w = W

print(ans)