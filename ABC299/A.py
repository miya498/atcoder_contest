N = int(input())
S = input()

flag = False
ans = False
for i in range(N):
    if S[i] == "|" and flag == False:
        flag = True
    elif S[i] == "|" and flag == True:
        flag = False

    if flag and S[i] == "*":
        ans = True

if ans:
    print("in")
else:
    print("out")