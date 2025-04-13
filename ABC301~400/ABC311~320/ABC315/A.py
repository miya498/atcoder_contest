S = list(input())

ans = []
moji = ["a","e","i","o","u"]

for i in range(len(S)):
    if S[i] not in moji:
        ans.append(S[i])

print("".join(ans))
