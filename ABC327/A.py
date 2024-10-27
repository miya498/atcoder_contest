N = int(input())
S = input()

flag = False

for i in range(1,N):
    if S[i-1] == 'a':
        if S[i] == 'b':
            flag = True
    elif S[i-1] == 'b':
        if S[i] == 'a':
            flag = True

if flag:
    print("Yes")
else:
    print("No")