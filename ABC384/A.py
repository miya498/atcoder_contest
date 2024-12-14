N,C,c = input().split()
S = input()

ans = ""

for i in range(int(N)):
    if S[i] == C:
        ans += C
    else:
        ans += c
print(ans)