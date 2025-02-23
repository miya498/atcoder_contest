N = int(input())
name = set()

for _ in range(N):
    s,t = input().split()
    name.add((s,t))

if len(name) == N:
    print("No")
else:
    print("Yes")