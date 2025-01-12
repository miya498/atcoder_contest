X,A,D,N = map(int,input().split())

min_A = A
max_A = A+D*(N-1)

if min_A > max_A:
    min_A,max_A = max_A,min_A

if X <= min_A:
    print(min_A-X)
elif X >= max_A:
    print(X-max_A)
else:
    diff = abs(D)
    amari = (X-A)%diff
    print(min(amari,diff-amari))