N = int(input())
A = list(map(int, input().split()))

A.sort()
total_sum = sum(A)
min_difference = float('inf')

for mask in range(1,2**N):
    group1_sum = 0
    for i in range(N):
        if mask & (1 << i):
            group1_sum += A[i]
    group2_sum = total_sum - group1_sum
    difference = max(group1_sum,group2_sum)
    min_difference = min(min_difference, difference)

print(min_difference)