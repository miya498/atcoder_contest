N,K = map(int,input().split())
S = list(input())

ans = 0

i = 0

while i <= N-K:
    if all(S[j] == 'O' for j in range(i,i+K)):
        for j in range(i,i+K):
            S[j] = 'X'

        ans += 1
        i += K
    else:
        i += 1

print(ans)