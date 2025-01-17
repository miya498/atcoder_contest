N,A,B = map(int,input().split())

ans = [[] for _ in range(A*N)]
for i in range(A*N):
    for j in range(B*N):
        if (i//A)%2 == 0:
            if (j//B)%2 == 0:
                ans[i].append(".")
            else:
                ans[i].append("#")
        else:
            if (j//B)%2 == 0:
                ans[i].append("#")
            else:
                ans[i].append(".")

for s in ans:
    print("".join(s))

