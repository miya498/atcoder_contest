N = int(input())

d = list()

for i in range(N):
    d.append(input())

d = list(set(d))
d.sort(reverse=True)

print(len(d))    