N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort()

left,right = 0,max(A[-1],B[-1])+1

while left < right:
    mid = (left+right)//2

    sellers = sum(1 for a in A if a <= mid)
    buyers = sum(1 for b in B if b >= mid)

    if sellers >= buyers:
        right = mid
    else:
        left = mid + 1


print(left)