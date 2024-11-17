S = input()

A = []
cnt = 0
for i in range(len(S)):
    if S[i] == "-":
        cnt += 1
    elif S[i] == "|" and i != 0:
        A.append(cnt)
        cnt = 0
    
print(*A)