N = int(input())
D = list(map(int,input().split()))

ans = 0

for i,d in enumerate(D):
    month_str = str(i+1)
    for j in range(d):
        day_str = str(j+1)
        if len(set(month_str+day_str)) == 1:
            ans += 1
print(ans)
