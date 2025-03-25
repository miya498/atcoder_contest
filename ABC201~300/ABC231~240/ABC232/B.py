S = input()
T = input()

if len(S) != len(T):
    print("No")
    exit()

K = (ord(T[0]) - ord(S[0])) % 26  

for i in range(len(S)):
    if (ord(T[i]) - ord(S[i])) % 26 != K:
        print("No")
        exit()

print("Yes")