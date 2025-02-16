S = input()
ans = []

for i in range(len(S)):
    s = S[i:]+S[:i]
    ans.append(s)
ans.sort()

print(ans[0])
print(ans[-1])