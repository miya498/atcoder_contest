def dfs():
    global lst
    if len(lst) == N:
        ans.append(lst.copy())
    elif len(lst) == 0:
        for i in range(1,11):
            lst.append(i)
            dfs()
            lst.pop()
    else:
        key = lst[-1]
        maxi = M - 10*(N-len(lst)-1)
        for i in range(key+10,maxi+1):
            lst.append(i)
            dfs()
            lst.pop()

N, M = map(int, input().split())
ans = []
lst = []
dfs()

print(len(ans))
for i in ans:
    print(*i)