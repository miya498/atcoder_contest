N = int(input())
card_array = []
for i in range(1, N + 1):
    a, c = map(int, input().split())
    card_array.append((c, a, i))

card_array.sort()
ans_lst = []
max_power = -1
for card in card_array:
    cost, power, card_number = card
    if max_power < power:
        max_power = power
        ans_lst.append(card_number)

ans_lst.sort()
print(len(ans_lst))
print(*ans_lst)