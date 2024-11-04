N = int(input())

S = []

for i in range(N+1):
    s = "-"
    for j in range(1,10):
        if i%(N/j) == 0:
            s = str(j)
            break
    S.append(s)

ans = "".join(S)

print(ans)