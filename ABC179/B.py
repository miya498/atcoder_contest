N = int(input())
D = [list(map(int,input().split())) for _ in range(N)]

for i in range(1,N-1):
    if D[i-1][0] == D[i-1][1] and D[i][0] == D[i][1]  and D[i+1][0] == D[i+1][1]:
        print("Yes")
        exit()
print("No")
