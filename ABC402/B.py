Q = int(input())

line = []
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        X = query[1]
        line.append(X)
    elif query[0] == 2:
        print(line[0])
        line.pop(0)
