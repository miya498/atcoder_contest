N, M = map(int, input().split())
A = list(map(int, input().split()))

num = [0] * (M+1)
syurui = 0

first_full = None
for i,x in enumerate(A,start=1):
    if 1 <= x <= M:
        num[x] += 1
        if num[x] == 1:
            syurui += 1
    if syurui == M:
        first_full = i
        break

if first_full is None:
    print(0)
else:
    print(N-first_full+1)
