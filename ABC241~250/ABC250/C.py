N,Q = map(int,input().split())
X = [int(input()) for _ in range(Q)]

balls = list(range(1,N+1))
pos =  list(range(N))

for x in X:
    idx = pos[x-1]

    if idx < N-1:
        swap = idx + 1
    else:
        swap = idx - 1
    
    balls[idx],balls[swap] = balls[swap],balls[idx]
    pos[balls[idx]-1],pos[balls[swap]-1] = pos[balls[swap]-1],pos[balls[idx]-1]

print(*balls)
