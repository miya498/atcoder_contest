N = int(input())

num = []
for _ in range(N):
    t,l,r = map(int,input().split())
    if t == 2:
        r -= 0.1
    elif t == 3:
        l += 0.1
    elif t == 4:
        l += 0.1
        r -= 0.1
    num.append([l,r])

ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        if num[i][0] < num[j][0]:
            if num[i][1] < num[j][0]:
                continue
            else:
                ans += 1
        else:
            if num[j][1] < num[i][0]:
                continue
            else:
                ans += 1
print(ans)