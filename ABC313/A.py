N = int(input())
P = list(map(int,input().split()))

max_score = 0
for i in range(1,N):
    max_score = max(max_score,P[i])

if max_score < P[0]:
    print(0)
else:
    print(max_score+1-P[0])