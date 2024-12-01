N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

lst = [(b_i, i) for i, b_i in enumerate(B)]
lst.sort(reverse=True)

ans = [-1] * M
ind = 0
for i, a in enumerate(A, 1):
    while ind < M and lst[ind][0] >= a:
        ans[lst[ind][1]] = i
        ind += 1

for ans_i in ans:
    print(ans_i)