N,Q = map(int,input().split())
hato_su = list(range(N+1))
cnt = [1]*(N+1)
su = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        P,H = query[1],query[2]
        old_su = hato_su[P]

        cnt[old_su] -= 1
        if cnt[old_su] == 1:
            su -= 1
        hato_su[P] = H
        cnt[H] += 1
        if cnt[H] == 2:
            su += 1
    elif query[0] == 2:
        print(su)