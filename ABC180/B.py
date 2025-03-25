import math
N = int(input())
X = list(map(int,input().split()))
m_dis = 0
y_dis = 0
c_dis = 0
for x in X:
    m_dis += abs(x)
    y_dis += x**2
    if c_dis < abs(x):
        c_dis = abs(x)

y_dis = math.sqrt(y_dis)
print(m_dis)
print(y_dis)
print(c_dis)