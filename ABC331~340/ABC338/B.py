from collections import Counter

def most_frequent_char(s):
    count = Counter(s)
    max_char = sorted(count.items(),key=lambda x: (-x[1],x[0]))
    return max_char[0][0]

S = input()
print(most_frequent_char(S))

