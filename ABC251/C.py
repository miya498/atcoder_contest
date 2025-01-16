N = int(input())
S = []
T = []

for _ in range(N):
    s,t = input().split()
    S.append(s)
    T.append(int(t))

best_idx = -1
best_score = -1

original = set()

for i in range(N):
    if S[i] in original:
        continue
    original.add(S[i])
    if best_score < T[i]:
        best_idx = i+1
        best_score = T[i]

print(best_idx)

