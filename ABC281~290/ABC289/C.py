N,M=[int(nm) for nm in input().split()]
ok=[[] for _ in range(N+1)]
S=[]
for i in range(M):
    C=int(input())
    A=[int(a) for a in input().split()]
    S.append(set(A))

ans=0
# 選び方全探索
for bit in range(2**M):
    #　個の選び方で x が含まれるか管理
    ok=[False for _ in range(N+1)]
    
    for i in range(M):
        # Si を選んでいるか
        if bit>>i & 1:
            for s in S[i]:
                ok[s]=True
    
    # 1～N まで全てあれば条件を満たす選び方として計上
    if all(ok[1:]):
        ans+=1

print(ans)