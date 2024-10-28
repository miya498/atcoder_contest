N = int(input())
A = list(map(int, input().split()))

# 重複を排除してリストに変換
lis = set(A)

# リストを降順でソート
ans = sorted(lis, reverse=True)

print(ans[1])
