N = int(input())
A = list(map(int, input().split()))
n = set(A)
if N == len(n):
    print("Yes")
else:
    print("No")