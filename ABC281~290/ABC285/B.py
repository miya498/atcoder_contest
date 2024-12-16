N = int(input())
S = input()

for i in range(1,N):
    ans = 0
    j = 0
    while i+j < N:
        if S[j] == S[i+j]:
            break
        j += 1
        ans += 1
    print(ans) 