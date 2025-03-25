A,B,K = map(int,input().split())

cnt = 0
if A >= B:
        print(cnt)
        exit()
        
while True:
    A *= K
    cnt += 1
    if A >= B:
        print(cnt)
        exit()