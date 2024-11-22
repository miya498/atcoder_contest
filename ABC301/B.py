N = int(input())
A = list(map(int, input().split()))

i = 0

while i < len(A) - 1:
    if abs(A[i] - A[i + 1]) > 1:  # 差が1以上なら補完が必要
        if A[i] < A[i + 1]:
            B = list(range(A[i] + 1, A[i + 1]))
        else:
            B = list(range(A[i] - 1, A[i + 1], -1))
        A = A[:i + 1] + B + A[i + 1:]  # 補完リストを挿入
    i += 1

print(*A)