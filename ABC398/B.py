from collections import Counter
a,b,c,d,e,f,g = map(int,input().split())
card = [a,b,c,d,e,f,g]
card_cnt = Counter(card)

for card,cnt in card_cnt.items():
    if cnt >= 3:
        for ca,cn in card_cnt.items():
            if ca != card and cn >= 2:
                ans = True
                print("Yes")
                exit()
print("No")
