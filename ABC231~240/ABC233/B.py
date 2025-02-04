L,R = map(int,input().split())
S = list(input())
s = S[L-1:R]
s.reverse()

ans = S[:L-1]+s+S[R:]
print("".join(ans))
