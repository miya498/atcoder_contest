N = int(input())
W = list(map(int,input().split()))
S1 = 0
ans = float('inf')
for i in range(1,N):
    S1 += W[i-1]
    S2 = sum(W)-S1
    ans = min(ans,abs(S1-S2))
print(ans)
