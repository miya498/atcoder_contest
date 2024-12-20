from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)
B=sorted(list(set(A)),reverse=True)

for n in B:
  print(cnt[n])
for i in range(N-len(B)):
  print(0)
