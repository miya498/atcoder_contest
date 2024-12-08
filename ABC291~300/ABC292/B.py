N,Q = map(int,input().split())

player = [0]*N

for i in range(Q):
    querys = list(map(int,input().split()))
    if querys[0] == 1:
        player[querys[1]-1] += 1

    elif querys[0] == 2:
        player[querys[1]-1] += 2
    elif querys[0] == 3:
        if player[querys[1]-1] >= 2:
            print("Yes")
        else:
            print("No")

