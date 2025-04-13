N,M = map(int,input().split())
H = list(map(int,input().split()))

sum = 0
for i in range(N):
    sum += H[i]
    if sum > M:
        print(i)
        break

if sum <= M:
    print(N)