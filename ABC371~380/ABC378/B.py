N = int(input())
Q = []
R = []

# 各条件 (q, r) の入力を受け取る
for i in range(N):
    q, r = map(int, input().split())
    Q.append(q)
    R.append(r)

question = int(input())

# 各質問 (t, d) に対して何日後に回収されるかを計算
for _ in range(question):
    t, d = map(int, input().split())
    t -= 1
    cnt = d//Q[t]
    if d >Q[t]*cnt+R[t]:
        ans = Q[t]*(cnt+1)+R[t]
    else:
        ans = Q[t]*cnt+R[t]
    print(ans)        
    