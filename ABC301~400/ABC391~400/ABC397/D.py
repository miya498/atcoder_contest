from math import sqrt
N = int(input())
found = False

d_max = int(N**(1/3))+2

for d in range(1,d_max):
    if d**3 > N:
        break

    D = 12*N*d -3*d**4
    if D < 0 or int(sqrt(D))*int(sqrt(D)) != D:
        continue
    num = -3*d**2 + int(sqrt(D))
    if num <= 0:
        continue
    if num % (6 * d) != 0:
        continue
    y = num // (6 * d)
    if y <= 0:
        continue
    x = y+d
    if x**3 - y**3 == N:
        print(x, y)
        found = True
        break

if not found:
    print(-1)
