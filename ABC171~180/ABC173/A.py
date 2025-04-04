N = int(input())
ans = 0
for i in range(1,11):
    ans += 1000
    if ans >= N:
        print(ans-N)
        exit()
