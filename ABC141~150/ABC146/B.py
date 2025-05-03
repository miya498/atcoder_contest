N = int(input())
S = input()
ans = ""
for i in range(len(S)):
    ans += chr(ord("A") + (ord(S[i]) - ord("A") + N) % 26)

print(ans)
