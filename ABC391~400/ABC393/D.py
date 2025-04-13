N = int(input())
S = input()

positions = [i for i, ch in enumerate(S) if ch == '1']
k = len(positions)

median = positions[k // 2]
min_moves = sum(abs(positions[i] - (median + i - k // 2)) for i in range(k))

print(min_moves)
