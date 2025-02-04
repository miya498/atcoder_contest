from collections import Counter

N = int(input())
A = list(map(int,input().split()))

a = Counter(A)

for i in range(1,N+1):
    if a[i] == 3:
        print(i)
        exit()