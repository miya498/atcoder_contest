from collections import Counter

N,K = map(int,input().split())
C = list(map(int,input().split()))

k = Counter(C[:K])
ans = len(k)
for i in range(K,N):
    k[C[i]] += 1
    k[C[i-K]] -= 1
    if k[C[i-K]] == 0:
        del k[C[i-K]]
    ans = max(len(k),ans)
print(ans)