from collections import Counter

N = int(input())
A = list(map(int, input().split()))

a_counter = Counter(A)
ans = N * (N - 1) // 2

for value in a_counter.values():
    ans -= value * (value - 1) // 2

print(ans)