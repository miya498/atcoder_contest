N = int(input())
A = list(map(int,input().split()))

kaku = [0]
a = 0
for i in range(N):
    a = (a+A[i])%360
    kaku.append(a)
kaku.append(360)
kaku.sort()
ans = 0
for i in range(1,N+2):
    ans = max(ans,kaku[i]-kaku[i-1])
print(ans)