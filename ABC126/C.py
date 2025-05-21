import math

N,K = map(int,input().split())
ans = 0
for i in range(1,N+1):
    if i < K:
        if int(math.log2(K/i)) == math.log2(K/i):
            ans += (1/N) * (1/2)**int((math.log2(K/i)))
        else:
            ans += (1/N) * (1/2)**int((math.log2(K/i))+1)
    else:
        ans += (1/N)
print(ans)