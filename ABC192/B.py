S = input()
flag = True
for i in range(len(S)):
    if i%2 == 0 and S[i].isupper():
        flag = False
    elif i%2 == 1 and S[i].islower():
        flag = False

if flag:
    print("Yes")
else:
    print("No")
