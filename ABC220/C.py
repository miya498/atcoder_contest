N = int(input())
A = list(map(int,input().split()))
X = int(input())

cnt = X//(sum(A))
diff = X-sum(A)*cnt
sum_val = 0
for i in range(len(A)):
    sum_val += A[i]
    if sum_val > diff:
        print(N*cnt+i+1)
        break
