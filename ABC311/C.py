# 入力の読み込み
N = int(input())
A = list(map(int, input().split()))

# 頂点番号の調整（1-indexed から 0-indexed へ変換）
A = [a - 1 for a in A]

visited_list = [0]
visited_set = {0}

v = 0

while True:
    nv = A[v]
    #一度通った点のとき
    if nv in visited_set:
        idx = visited_list.index(nv)
        ans_list = visited_list[idx:]
        print(len(ans_list))
        print(*[a+1 for a in ans_list])
        break
    #初めて通った点のとき
    else:
        visited_set.add(nv)
        visited_list.append(nv)
        v = nv