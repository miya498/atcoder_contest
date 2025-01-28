S = input()

if S == S.upper() or S == S.lower():
    print("No")
    exit()

moji = set()

for i in range(len(S)):
    moji.add(S[i])

if len(S) == len(moji):
    print("Yes")
else:
    print("No")