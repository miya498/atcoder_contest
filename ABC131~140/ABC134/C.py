N = int(input())
A = [int(input()) for _ in range(N)]
B = sorted(A)
max_a = max(A)
max_index = A.index(max_a)

for i in range(N):
    if i == max_index:
        print(B[-2])
    else:
        print(max_a)
