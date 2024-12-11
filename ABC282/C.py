N = int(input())
S = input()

ans = ""
flag = False
for i in range(N):
    if S[i] == '"' and flag == False:
        flag = True
    elif S[i] == '"' and flag == True:
        flag = False

    if S[i] == "," and flag == False:
        ans += "."
    else:
        ans += S[i]

print(ans)
