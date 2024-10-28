S = input()

n = len(S)
if S[n-3:n] == "san":
    print("Yes")
else:
    print("No")