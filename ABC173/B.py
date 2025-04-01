N = int(input())
test = [input() for _ in range(N)]

ans = [0]*4
for s in test:
    if s == "AC":
        ans[0] += 1
    elif s == "WA":
        ans[1] += 1
    elif s == "TLE":
        ans[2] += 1
    else:
        ans[3] += 1

print(f"AC x {ans[0]}")
print(f"WA x {ans[1]}")
print(f"TLE x {ans[2]}")
print(f"RE x {ans[3]}")