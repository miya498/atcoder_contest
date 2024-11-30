S = list(map(int,input().split()))
flag = True

T = sorted(S)

if S != T :
    flag = False

if S[0] < 100 or S[7] > 676:
    flag = False

for i in range(8):
    if S[i] % 25 != 0:
        flag = False

if flag:
    print("Yes")
else:
    print("No")