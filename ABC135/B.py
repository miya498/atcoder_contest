N = int(input())
P = list(map(int,input().split()))

P_copy = P[:]

if P == sorted(P):
    print("YES")
    exit()

for i in range(N):
    for j in range(N):
        P_copy = P[:]
        if P[i] > P[j]:
            P_copy[i],P_copy[j] = P_copy[j],P_copy[i]

            if P_copy == sorted(P_copy):
                print("YES")
                exit()

print("NO")
