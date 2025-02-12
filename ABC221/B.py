S = input()
T = input()

flag = False
for i in range(len(S)-1):
    s = S[:i] + S[i+1] + S[i] + S[i+2:]
    if s == T:
        flag = True

if flag or S == T:
    print("Yes")
else:
    print("No")