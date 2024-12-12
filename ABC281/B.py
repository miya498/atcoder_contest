S = input()

if len(S) == 8:
    if S[0].isalpha() and S[1:7].isdigit() and S[7].isalpha():
        num = int(S[1:7])
        if 100000 <= num <= 999999 and S[0].isupper() and S[7].isupper():
            print("Yes")
            exit()

print("No")
    