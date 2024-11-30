N,D= map(int,input().split())
S = input()

cnt = 0
for i in range(N):
    if S[i] == "@":
        cnt += 1

ans = ""
at = 0
for i in range(N):
    if S[i] == "@":
        at += 1
        if at <= cnt-D:
            ans += "@"
        else:
            ans += "."
    else:
        ans += "."

print(ans)
    