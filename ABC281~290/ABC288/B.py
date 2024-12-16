N,K = map(int,input().split())

winner = []

for i in range(N):
    s = input()
    if i < K:
        winner.append(s)

winner.sort()

for s in winner:
    print(s)