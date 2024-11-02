N = int(input())
S = input()
flag = False
for i in range(N-2):
    if S[i:i+3] == "ABC":
        print(i+1)
        flag = True
        break

if flag != True:
    print(-1)    