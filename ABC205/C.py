A, B, C = map(int, input().split())

if C % 2 == 0:  # Cが偶数なら絶対値を比較
    if abs(A) < abs(B):
        print("<")
    elif abs(A) > abs(B):
        print(">")
    else:
        print("=")
else:  # Cが奇数ならそのまま比較
    if A < B:
        print("<")
    elif A > B:
        print(">")
    else:
        print("=")