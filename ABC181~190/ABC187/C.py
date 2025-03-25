N = int(input())
S = []
S_a = set()
for _ in range(N):
    s = input()
    if s[0] == "!":
        S_a.add(s)
    else:
        S.append(s)

for s in S:
    human = "!" + s
    if human in S_a:
        print(s)
        exit()
print("satisfiable")