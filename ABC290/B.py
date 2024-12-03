N,K = map(int,input().split())

S = input()

T = ""
cnt = 0
for i in range(N):
    if S[i] == "x":
        T += "x"
    elif S[i] == "o" and cnt < K:
        T += "o"
        cnt += 1
    elif S[i] == "o" and cnt >= K:
        T += "x"

print(T)

