N = int(input())
if N >= 42:
    ans = str(N+1)
    print('AGC'+ans.zfill(3))
else:
    print('AGC'+str(N).zfill(3))