N,A,B = map(int,input().split())

C = list(map(int,input().split()))

ans = A+B

for i  in range(N):
    if ans == C[i]:
        print(i+1)
        break