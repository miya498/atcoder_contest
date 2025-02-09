N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# Q の各要素のインデックスを辞書で管理（O(N)）
Q_index = {value: Q[P[i]-1] for i, value in enumerate(Q)}

ans = []
for i in range(N):
    ans.append(Q_index[i+1])

print(*ans)