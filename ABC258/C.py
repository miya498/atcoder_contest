N, Q = map(int, input().split())
S = input()
offset = 0  

for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        n = int(query[1])
        offset = (offset + n) % N  
    elif query[0] == "2":
        idx = (int(query[1])-1-offset)%N
        print(S[idx])