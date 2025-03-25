N = input()
ans = 0
for i in range(1<<len(N)):
    l = ""
    r = ""
    for j in range(len(N)):
        if i & (1<<j):
            l += N[j]
        else:
            r += N[j]
    if l and r:
        ans = max(ans,int(l)*int(r))
print(ans)