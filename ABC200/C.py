from collections import Counter
N = int(input())
A = list(map(int,input().split()))
for i in range(N):
    A[i] %= 200

a = Counter(A)
ans = 0
for v in a.values():
    ans += (v*(v-1))//2
print(ans)