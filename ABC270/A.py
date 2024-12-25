A,B = map(int,input().split())

A =  '{:03b}'.format(A)
B =  '{:03b}'.format(B)
ans = 0

for i in range(3):
    if A[i] == "1" or B[i] == "1":
        ans += 2**(2-i)
print(ans)

