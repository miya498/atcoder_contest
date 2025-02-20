N = int(input())
A = list(map(int,input().split()))

a = sorted(A,reverse=True)[1]

idx = A.index(a)+1
print(idx)