N, K = map(int, input().split())
A = [(1, 0)]
cnt = 0
for _ in range(N):
    a, b = map(int, input().split())
    A.append((a + 1, b))
    cnt += b
A.sort()

for a, b in A:
    cnt -= b
    if cnt <= K:
        print(a)
        exit()