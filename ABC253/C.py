from collections import Counter
from sortedcontainers import SortedList

Q = int(input())
S = Counter()
sorted_S = SortedList()

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x = query[1]
        if S[x] == 0:
            sorted_S.add(x)
        S[x] += 1

    elif query[0] == 2:
        x, c = query[1], query[2]
        if S[x] > 0:
            remove_count = min(c, S[x])
            S[x] -= remove_count
            if S[x] == 0:
                sorted_S.remove(x)

    elif query[0] == 3:
        print(sorted_S[-1] - sorted_S[0])