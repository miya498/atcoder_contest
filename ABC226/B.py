N = int(input())
A = set()
for _ in range(N):
    a = tuple(map(int,input().split()[1:]))
    A.add(a)

print(len(A))