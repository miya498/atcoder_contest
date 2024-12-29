K = int(input())
S = input()
T = input()

if S == T:
    print("Yes")
elif abs(len(S) - len(T)) > 1:
    print("No")
elif len(S) == len(T):
    diff_count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            diff_count += 1
    if diff_count == 1:
        print("Yes")
    else:
        print("No")
else:
    if len(S) < len(T):
        short,long = S, T
    else:
        short,long = T, S
    j=0
    mismatch_found = False
    for i in range(len(short)):
        if short[i] != long[j]:
            if mismatch_found:
                print("No")
                exit()
            mismatch_found = True
            j += 1
        j += 1

    print("Yes")