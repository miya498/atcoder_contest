import math
A,B,H,M = map(int,input().split())

A_angle = H*30 + M*0.5
B_angle = M*6
angle = abs(A_angle-B_angle)
if angle>180:
    angle = 360 - angle

ans = math.sqrt(A**2+B**2-2*A*B*math.cos(angle*math.pi/180))
print(ans)