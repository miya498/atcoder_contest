N = int(input())
S = input()

flag_1 = False
flag_2 = True

for i in range(N):
    if S[i] == "x":
        flag_2 = False

    if S[i] == "o":
        flag_1 = True

if flag_1 and flag_2:
    print("Yes") 
else:
    print("No")