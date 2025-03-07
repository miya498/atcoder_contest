N = int(input())
S = list(input())
Q = int(input())
queries = [list(map(int,input().split())) for _ in range(Q)]
flag = False
for q in queries:
    if q[0] == 1:
        a,b = q[1]-1,q[2]-1
        if flag:
            a = a+N
            b = b-N
        S[a],S[b] = S[b],S[a]
    elif q[0] == 2:
        if flag:
            flag = False
        else:
            flag = True

if flag:
    S = S[N:]+S[:N]
print("".join(S))