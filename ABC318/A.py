N,M,P = map(int,input().split())

cnt = 0
day = 0

while True:
    if cnt == 0:
        if M <= N:
            day += M
            cnt += 1
        else:
            break
    else:
        day += P
        if day <= N:
            cnt += 1
        else:
            break

print(cnt)

