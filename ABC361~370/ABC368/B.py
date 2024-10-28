N = int(input())
A = list(map(int, input().split()))

count = 0
while True:
    A.sort(reverse=True)  # 大きい順にソート
    if A[1] <= 0:  # 2番目に大きい要素が0以下になったら終了
        break
    A[0] -= 1  # 一番大きい要素を減らす
    A[1] -= 1  # 2番目に大きい要素を減らす
    count += 1

print(count)