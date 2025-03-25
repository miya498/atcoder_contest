N,X = map(int,input().split())
X *= 100
V,P = [],[]
for _ in range(N):
    v,p = map(int,input().split())
    V.append(v)
    P.append(p)
alch_sum = 0
for i in range(N):
    alch_sum += V[i]*P[i]
    if alch_sum > X:
        print(i+1)
        exit()
print(-1)
