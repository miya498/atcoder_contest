import itertools

N,M = map(int,input().split())
x_list = set()

for _ in range(M):
    k = list(map(int,input().split()))
    for v in itertools.combinations(k[1:],2):
        x_list.add(v)

if len(x_list) == N*(N-1)//2:
    print("Yes")
else:
    print("No")



