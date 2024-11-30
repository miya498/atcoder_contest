N = int(input())

if N <= 10**3-1:
    print(N)
elif 10**3 <= N <= 10**4-1:
    ans = N-N%10
    print(ans)
elif 10**4 <= N <= 10**5-1:
    ans = N-N%100
    print(ans)
elif 10**5 <= N <= 10**6-1:
    ans = N-N%1000
    print(ans)
elif 10**6 <= N <= 10**7-1:
    ans = N-N%10000
    print(ans)
elif 10**7 <= N <= 10**8-1:
    ans = N-N%100000
    print(ans)
elif 10**8 <= N <= 10**9-1:
    ans = N-N%1000000
    print(ans)
