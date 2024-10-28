N,M = map(int,input().split())
A = list(map(int,input().split()))

def is_valid(x):
    total = 0
    for a in A:
        total += min(a,x)
    return total <= M

total = sum(A)
A.sort(reverse=True)

if total <= M:
    print("infinite")
else:
    low,high = 0,A[0]

    while low<=high:
        mid =(low+high)//2
        if is_valid(mid):
            low = mid+1
        else:
            high = mid-1
    print(high)
