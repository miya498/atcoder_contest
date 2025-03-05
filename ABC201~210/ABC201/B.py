N = int(input())
S_T = []
for _ in range(N):
    s,t = input().split()
    S_T.append([s,int(t)])
S_T.sort(key=lambda x: (-x[1],x[0]))

print(S_T[1][0])