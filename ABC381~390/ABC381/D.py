from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

count = defaultdict(int)
left = N - 1
ans = 0

for right in range(N - 1, -1, -1):
    count[A[right]] += 1
    while any(count[x] > 2 for x in count):
        count[A[left]] -= 1
        if count[A[left]] == 0:
            del count[A[left]]
        left -= 1
    if all(v == 2 for v in count.values()):
        ans = max(ans, left - right + 1)

print(ans)