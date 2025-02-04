import math

N = int(input())
if N > 2*math.log2(N):
    print("Yes")
else:
    print("No")