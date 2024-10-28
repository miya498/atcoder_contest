A,M,L,R = map(int,input().split())

L = L - A
R = R - A

ans = R//M - (L-1)//M
 
print(ans)