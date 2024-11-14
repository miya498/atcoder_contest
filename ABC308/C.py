N = int(input())
A_B = []
for i in range(N):
    a,b = map(int,input().split())
    if b != 0:
        dev = a/b
        A_B.append([dev,i+1])
    else:
        dev = 1
        A_B.append([dev,i+1])

A_B.sort(key=lambda x: (-x[0],x[1]))
ans = []
for i in range(N):
    ans.append(A_B[i][1])

print(*ans)



