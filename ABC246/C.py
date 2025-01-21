N,K,X = map(int,input().split())
A = list(map(int,input().split()))

ticket = 0

for i in range(N):
    cnt = A[i]//X
    if K < ticket+cnt:
        A[i] -= (K-ticket)*X
        print(sum(A))
        exit()
    else:
        A[i] -= cnt*X
        ticket += cnt

if ticket == K:
    print(sum(A))

else:
    A.sort(reverse=True)
    for i in range(min(K-ticket,N)):
        A[i] = 0
    
    print(sum(A))
