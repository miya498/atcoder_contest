N = int(input())
if N % 2==0:
    ans = "-"*((N-2)//2)+"=="+"-"*((N-2)//2)
else:
    ans = "-"*((N-1)//2)+"="+"-"*((N-1)//2)
print(ans)