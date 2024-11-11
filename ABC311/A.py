N = int(input())
S = input()

A_flag = False
B_flag = False
C_flag = False

for i in range(N):
    if S[i] == "A":
        A_flag = True

    if S[i] == "B":
        B_flag = True

    if S[i] == "C":
        C_flag = True
    
    if A_flag and B_flag and C_flag:
        print(i+1)
        exit()
            