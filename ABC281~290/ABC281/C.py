N,T = map(int,input().split())
A = list(map(int,input().split()))
music = [0]
cnt = 0
for i in range(N):
    cnt += A[i]
    music.append(cnt)
end = sum(A)

amari = T%end

for i in range(N+1):
    if amari <= music[i]:
        print(i,amari-music[i-1])
        exit()

