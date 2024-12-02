S = input()
T = S.upper()

for i in range(len(S)):
    if S[i] == T[i]:
        print(i+1)