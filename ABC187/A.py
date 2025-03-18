A,B = input().split()

s_a = 0
for i in range(len(A)):
    s_a += int(A[i])
s_b = 0
for i in range(len(B)):
    s_b += int(B[i])

print(max(s_a,s_b))

