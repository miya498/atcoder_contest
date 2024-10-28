M, D = map(int,input().split())
y,m,d = map(int,input().split())

cur_y = y
cur_m = m
cur_d = d+1

if cur_d > D:
    cur_d = 1
    cur_m += 1

if cur_m > M:
    cur_m = 1
    cur_y += 1

print(cur_y,cur_m,cur_d)