N = int(input())
P = list(map(int,input().split()))
Q = [0 for _ in range(N)]

for i in range(N):
    Q[P[i]-1] = i+1

print(*Q)
