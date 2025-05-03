N,K = map(int, input().split())
H = list(map(int, input().split()))

H.sort(reverse=True)

ans = 0
for i in range(N):
    if H[i] >= K:
        ans += 1
    else:
        break

print(ans)
