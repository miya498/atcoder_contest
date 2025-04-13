N = int(input())
A = list(map(int,input().split()))

seen = {}
min_len = float("inf")
left = 0

for right in range(N):
    if A[right] in seen and seen[A[right]] >= left:
        min_len = min(min_len,right-seen[A[right]]+1)
        left = seen[A[right]] + 1

    seen[A[right]] = right

if min_len == float("inf"):
    print(-1)
else:
    print(min_len)