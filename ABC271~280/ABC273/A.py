def cal(n):
    if n == 0:
        return 1
    
    return n * cal(n - 1)

N = int(input())

ans = cal(N)

print(ans)

