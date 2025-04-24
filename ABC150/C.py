import itertools

N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))

A = list(itertools.permutations(range(1,N+1)))
a = 0
b = 0
A.sort()

for i,num in enumerate(A):
    if num == P:
        a = i
    if num == Q:
        b = i

print(abs(a-b))