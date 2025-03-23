from itertools import permutations

N,K = map(int,input().split())
T = [list(map(int,input().split())) for _ in range(N)]

data = [i for i in range(1,N)]
ans = 0
for perm in permutations(data):
    now_state = 0
    t = 0
    for p in perm:
        t += T[now_state][p]
        now_state = p
    t += T[now_state][0]
    if t == K:
        ans += 1

print(ans)
