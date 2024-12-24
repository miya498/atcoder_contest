N = int(input())
P = list(map(int,input().split()))

for i in range(N-2,-1,-1):
    if P[i] > P[i+1]:
        for j in range(N-1,i,-1):
            if P[j] < P[i]:
                P[i],P[j] = P[j],P[i]
                P = P[:i + 1] + sorted(P[i + 1:], reverse=True)  
                print(*P)
                exit()


