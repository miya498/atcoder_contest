N,K = map(int,input().split())
cnt = N//K
ans = min(abs(N-K*cnt),abs(N-K*(cnt+1)))

print(ans)