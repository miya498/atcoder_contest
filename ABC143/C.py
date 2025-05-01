N = int(input())
S = input()
ans = 1

slime = S[0]
for i in range(1, N):

    if S[i] != slime:
        ans += 1
        slime = S[i]

print(ans)
