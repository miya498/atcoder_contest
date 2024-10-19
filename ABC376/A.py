N,C = map(int,input().split())
T = list(map(int,input().split()))

cnt = 1
catch_time = T[0]

for i in range(1,N):
    if T[i]-catch_time >= C:
        cnt += 1
        catch_time = T[i]
print(cnt)