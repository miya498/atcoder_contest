S = input()
Sint = int(S[3:])
pre = 0
for i in range(1,350):
    if Sint==i:
        pre = 1

if Sint==316:
    pre = 0
if pre == 1:
    print("Yes")
else:
    print("No")