from collections import deque

Q = int(input())
queries = [input().split() for _ in range(Q)]

queue = deque()
offset = 0

for query in queries:
    if query[0] == "1":
        l = int(query[1])
        if not queue:
            head = 0
        else:
            head = queue[-1][0] + queue[-1][1]
        queue.append((head, l))
    elif query[0] == "2":
        _, length = queue.popleft()
        offset += length
    elif query[0] == "3":
        k = int(query[1]) - 1
        print(queue[k][0] - offset)