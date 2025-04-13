S = list(input())

flag = True
for i in range(1,16,2):
    if int(S[i])%2 != 0:
        flag = False

if flag:
    print("Yes")
else:
    print("No")