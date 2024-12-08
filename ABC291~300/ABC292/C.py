from collections import defaultdict

n = int(input())
m = defaultdict(int)
for a in range(1, n):
    b = 1
    while a * b < n:
        m[a * b] += 1
        b += 1

result = 0
for k, v in m.items():
    cd = n - k
    if cd in m:
        result += v * m[cd]

print(result)