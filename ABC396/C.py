N,M = map(int,input().split())
B = list(map(int,input().split()))
W = list(map(int,input().split()))

black_pos = []
black_neg = []

for b in B:
    if b >= 0:
        black_pos.append(b)
    else:
        black_neg.append(b)

black_pos.sort(reverse=True)
black_neg.sort(reverse=True)

white_pos = [w for w in W if w > 0]
white_pos.sort(reverse=True)

sum_black = sum(black_pos)
cnt_black = len(black_pos)

white_cnt = min(cnt_black,len(white_pos))
sum_white = sum(white_pos[:white_cnt])

ans = sum_black+sum_white
index = white_cnt

for b in black_neg:
    if index < len(white_pos):
        if white_pos[index]+b > 0:
            sum_black += b
            cnt_black += 1
            sum_white += white_pos[index]
            index += 1
            ans = max(ans,sum_black+sum_white)
    else:
        break
print(max(ans,0))
