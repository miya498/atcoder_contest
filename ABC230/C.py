N,A,B = map(int,input().split())
P,Q,R,S = map(int,input().split())

ans = [["."]*(S-R+1) for _ in range(Q-P+1)]

k_1_min = max(1-A,1-B)
k_1_max = min(N-A,N-B)
k_2_min = max(1-A,B-N)
k_2_max = min(N-A,B-1)

for i in range(Q-P+1):
    for j in range(S-R+1):
        x = i+P
        y = j+R
        if y-x == B-A and k_1_min <= x-A <= k_1_max:
            ans[i][j] = "#"
        if A+B == x+y and k_2_min <= x-A <= k_2_max:
            ans[i][j] = "#"

for a in ans:
    print("".join(a))