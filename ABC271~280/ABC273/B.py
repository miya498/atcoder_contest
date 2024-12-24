X,K = map(int,input().split())

for i in range(K):
    p = 10**(i+1)
    X = (X+p//2)//p*p
print(X)