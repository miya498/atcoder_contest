N,M = map(int,input().split())
ans = 0
for i in range(M+1):
    ans += N**i
    if ans > 1000000000:
        print("inf")
        exit()
print(ans)