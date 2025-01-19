import math

a, b, d = map(int, input().split())

theta = math.radians(d)

x_new = a * math.cos(theta) - b * math.sin(theta)
y_new = a * math.sin(theta) + b * math.cos(theta)

print(x_new, y_new)