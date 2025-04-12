N = int(input())
S = [input() for _ in range(N)]
status = False
ans = 0
for i in range(N):
    if S[i] == "login":
        status = True
    elif S[i] == "logout":
        status = False
    elif not status and S[i] == "private":
        ans += 1

print(ans)
