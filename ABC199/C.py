N = int(input())
S = list(input())
Q = int(input())
queries = [list(map(int,input().split())) for _ in range(Q)]

for q in queries:
    if q[0] == 1:
        a,b = q[1]-1,q[2]-1
        S[a],S[b] = S[b],S[a]
    elif q[0] == 2:
        S = S[N:]+S[:N]

print("".join(S))

