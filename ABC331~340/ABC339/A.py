S = list(input())
n = len(S)
for i in range(n):
    if S[n-1-i] == ".":
        ans = "".join(S[n-i:])
        print(ans)
        break