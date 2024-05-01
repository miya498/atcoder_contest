def bubble_sort(arr):
    n = len(arr)
    swaps = 0
    swap_positions = []

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
                swap_positions.append((i+1,j+1))

    return swaps, swap_positions

# 入力を受け取る
N = input()

# スペースで区切ってリストに変換する
input_array = list(map(int, input().split()))

# 入れ替え回数と場所を計算する
swaps, swap_positions = bubble_sort(input_array.copy())

# 入れ替え回数を出力
print(swaps)

# 入れ替えた場所を出力
for swap in swap_positions:
    a=swap[0]
    b=swap[1]
    print(a ,b)

