T = int(input())
N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

if N < M:
    print("no")
    exit()

i = 0  # たこ焼きのインデックス
for j in range(M):  # お客さんのループ
    while i < N and A[i] + T < B[j]:  # 期限切れのたこ焼きをスキップ
        i += 1
    if i >= N or A[i] > B[j]:  # たこ焼きが足りない or お客さんが受け取れない
        print("no")
        exit()
    i += 1  # たこ焼きを売る

print("yes")

