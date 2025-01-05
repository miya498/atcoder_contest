N = int(input())
string = {}
S = []

for _ in range(N):
    s = input()
    S.append(s)
for s in S:
    if s in string:
        string[s] += 1
        print(f'{s}({string[s]})')
    else:
        string[s] = 0
        print(s)


