import math

def lcm(x,y):
    return x*y//math.gcd(x,y)

A,B,C,D = map(int,input().split())

ans_C = B//C - (A-1)//C
ans_D = B//D - (A-1)//D

ans_CD = B//lcm(C,D) - (A-1)//lcm(C,D)

print(B-A+1-(ans_C+ans_D-ans_CD))

