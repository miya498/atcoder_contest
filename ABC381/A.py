N = int(input())

S = input()
flag = True

if len(S)%2==1:
    for i in range(N):
        if (N+1)//2-1 > i:
            if S[i] != "1":
                flag = False
        elif (N+1)//2-1 == i:
            if S[i] != "/":
                flag = False
        else:
            if S[i] != "2":
                flag = False
else:
    flag = False

if flag:
    print("Yes")
else:
    print("No")
    