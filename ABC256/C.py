h_1,h_2,h_3,w_1,w_2,w_3 = map(int,input().split())
ans = 0
for a in  range(1,31):
    for b in range(1,31):
        for d in range(1,31):
            for e in range(1,31):
                c = h_1-a-b
                g = w_1-a-d
                f = h_2-d-e
                h = w_2-b-e
                if c >= 1 and g >= 1 and f >= 1 and h >= 1:
                    if h_3-g-h == w_3-c-f and h_3-g-h > 0:
                        ans += 1

print(ans)
                