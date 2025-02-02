from collections import Counter

N = int(input())
S = [input() for _ in range(N)]
s = Counter(S)
print(s.most_common()[0][0])