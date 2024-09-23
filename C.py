N, Q = map(int, input().split())
S = list(input())

abc_count = 0
for i in range(N - 2):
    if S[i:i+3] == ['A', 'B', 'C']:
        abc_count += 1

for _ in range(Q):
    X, C = input().split()
    X = int(X) - 1
    
    for i in range(max(0, X - 2), min(N - 2, X) + 1):
        if S[i:i+3] == ['A', 'B', 'C']:
            abc_count -= 1
            
    S[X] = C
    
    for i in range(max(0, X - 2), min(N - 2, X) + 1):
        if S[i:i+3] == ['A', 'B', 'C']:
            abc_count += 1

    print(abc_count)