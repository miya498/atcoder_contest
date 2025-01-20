N = int(input())
S, T = [], []

for _ in range(N):
    s, t = input().split()
    S.append(s)
    T.append(t)

for i in range(N):
    valid = False
    for a in [S[i], T[i]]:
        if all(a != S[j] and a != T[j] for j in range(N) if j != i):
            valid = True
            break
    if not valid:
        print("No")
        exit()

print("Yes")