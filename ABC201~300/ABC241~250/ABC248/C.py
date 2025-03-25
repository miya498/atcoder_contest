# pypyで提出

# 入力の受け取り
N,M,K=map(int,input().split())

# 余りの定義
mod=998244353

# (1)表を作る
dp=[[0]*(K+1) for i in range(N+1)]

# (2)すぐにわかるところを埋める
# ・(x≤M)dp[1][x]=1
# ・(M<x)dp[1][x]=0
for x in range(1,M+1):
    dp[1][x]=1

# (3)表の小さい方から答えにたどり着くまで埋める
# i=2~N
for i in range(2,N+1):
    # x=1~K
    for x in range(1,K+1):
        # a=(x-M)~(x-1)
        for a in range(x-M,x):
            # aが1未満のとき
            if a<1:
                # 次のaへ
                continue
            # ・(2≤i)dp[i][x]=(dp[i-1][x-M]~dp[i-1][x-1]の和)
            dp[i][x]+=dp[i-1][a]
            # 余りを取る
            dp[i][x]%=mod

# (4)答えを出力する
# 答え
ans=0

# x=1~K
for x in range(1,K+1):
    # dp[N][1]~dp[N][K]の和
    ans+=dp[N][x]
    # 余りを取る
    ans%=mod

# 答えを出力
print(ans)