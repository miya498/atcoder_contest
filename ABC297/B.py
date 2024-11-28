# 入力
S = input()

# 条件 1: B の偶奇の条件を確認
b_indices = [i for i, char in enumerate(S) if char == 'B']
if len(b_indices) == 2:
    b1, b2 = b_indices
    if (b1 % 2) == (b2 % 2):
        print("No")
        exit()
else:
    print("No")
    exit()

# 条件 2: K が 2 つの R の間にあることを確認
r_indices = [i for i, char in enumerate(S) if char == 'R']
k_index = S.index('K')

if len(r_indices) == 2:
    r1, r2 = r_indices
    if not (r1 < k_index < r2):
        print("No")
        exit()
else:
    print("No")
    exit()

# 条件を満たす場合
print("Yes")