N,M,Q = map(int, input().split())

view_list = [set() for _ in range(N)]
view_all = [False for _ in range(N)]
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        view_list[query[1]-1].add(query[2])
    elif query[0] == 2:
        view_all[query[1]-1] = True
    elif query[0] == 3:
        if view_all[query[1]-1] or query[2] in view_list[query[1]-1]:
            print("Yes")
        else:
            print("No")
