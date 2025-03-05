S = input()
ans = ""
for i in range(len(S)):
    if S[i] == "6":
        ans += "9"
    elif S[i] == "9":
        ans += "6"
    else:
        ans += S[i]

print(ans[::-1])
