import itertools

N,M = map(int,input().split())

for p in itertools.combinations(range(1,M+1),N):
    # 答えの出力(*をつけると[]なしで出力できる)
    print(*p)