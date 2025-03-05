N, K = map(int, input().split())
AB = []

for _ in range(N):
    A, B = map(int, input().split())
    AB.append([A,B])

AB.sort()

ans = K
for i in range(N):
    if ans < AB[i][0]:
        break
    else:
        ans += AB[i][1]
print(ans)