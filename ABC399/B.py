N = int(input())
P = list(map(int,input().split()))

ans = [0]*N
r = 1
while True:
    max_point = max(P)
    if max_point == 0:
        break
    cnt = 0
    for i in range(len(P)):
        if P[i] == max_point:
            ans[i] = r
            cnt += 1
            P[i] = 0
    r += cnt
for a in ans:
    print(a)