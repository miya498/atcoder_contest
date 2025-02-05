N,K = map(int,input().split())
P = [list(map(int,input().split())) for _ in range(N)]
total_score = [sum(p) for p in P]
copy = sorted(total_score,reverse=True)
k_score = copy[K-1]

for i in range(N):
    if k_score <= total_score[i]+300:
        print("Yes")
    else:
        print("No")