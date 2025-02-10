N = int(input())
A,B = [],[]

for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

time = 0

for i in range(N):
    time += A[i]/B[i]

time /= 2

ans = 0
t = 0
i = 0
while True:
    if A[i]/B[i]+t < time:
        t += A[i]/B[i]
        ans += A[i]
        i += 1
    else:
        ans += (time-t)*B[i]
        break
print(ans)






