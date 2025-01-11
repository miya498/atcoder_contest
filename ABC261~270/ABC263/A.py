card = list(map(int,input().split()))

card.sort()
ans = set(card)

if len(ans) == 2:
    if (card[1] == card[2] or card[2] == card[3]) and card[1] != card[3]:
        print("Yes")
        exit()

print("No")
