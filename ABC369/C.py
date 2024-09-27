N = int(input())
A = list(map(int,input().split(' ')))

ans = N + (N-1)

i = 0
while i < N-1:
    diff = A[i+1] - A[i]

    #連続する同じ差をカウント
    length = 1

    while i+length < N-1 and A[i+length+1]-A[i+length] == diff:
        length += 1
    
    ans += (length*(length-1))//2
    i += length

print(ans)