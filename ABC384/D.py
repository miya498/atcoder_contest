N,S = map(int,input().split())
A = list(map(int,input().split()))

a_sum = sum(A)
s = S%a_sum

cnt = 0
left = 0

for right in range(2*N):
    cnt += A[right%N]
    while cnt > s:
        cnt -= A[left%N]
        left += 1
    
    if cnt == s:
        print("Yes")
        exit()

print("No")
    
