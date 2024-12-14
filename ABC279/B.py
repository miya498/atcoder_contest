S = input()
T = input()

if S == T:
    print("Yes")
    exit()

for i in range(len(S) - len(T) + 1):
    for j in range(len(T)):
        if S[i + j] != T[j]:
            break
    else:  
        print("Yes")
        exit()

print("No")