N = int(input())
A = list(map(int, input().split()))

# 偶数と奇数を分類
even = []
odd = []

for a in A:
    if a % 2 == 0:
        even.append(a)
    else:
        odd.append(a)

# 最大の偶数の和を計算
max_even_sum = -1

# 偶数同士の和
if len(even) >= 2:
    even.sort(reverse=True)
    max_even_sum = max(max_even_sum, even[0] + even[1])

# 奇数同士の和
if len(odd) >= 2:
    odd.sort(reverse=True)
    max_even_sum = max(max_even_sum, odd[0] + odd[1])

print(max_even_sum)
