N = int(input())
v = list(map(int,input().split()))

v.sort()
while len(v) > 1:
    alchemist = (v[0] + v[1]) / 2
    v.pop(0)
    v.pop(0)
    v.append(alchemist)
    v.sort()

print(v[0])
