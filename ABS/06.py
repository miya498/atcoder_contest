N,A,B = map(int,input().split())

num = list()
for i in range(N+1):
    i = str(i)
    sum_degit = sum(int(digit) for digit in i)
    if A <= sum_degit and sum_degit <=B:
        num.append(int(i))
    
ans = sum(num)
print(ans)
