N,M = map(int,input().split())
P_S = []
for i in range(M):
    p,s = input().split()
    P_S.append([int(p),s])

AC = [False]*(N+1)
WA = [0]*(N+1)
AC_count = 0
WA_count = 0
for i in range(M):
    if P_S[i][1] == "AC" and not AC[P_S[i][0]]:
        AC[P_S[i][0]] = True
        AC_count += 1
    elif P_S[i][1] == "WA" and not AC[P_S[i][0]]:
        WA[P_S[i][0]] += 1

for i in range(N+1):
    if AC[i]:
        WA_count += WA[i]

print(AC_count,WA_count)