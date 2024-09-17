N = int(input())
A = list(map(int,input().split()))

Alice = 0
Bob = 0

A.sort(reverse=True)

for i in range(N):
    if i%2 == 0:
        Alice += A.pop(0)
    else:
        Bob += A.pop(0)

ans = Alice - Bob
print(ans)