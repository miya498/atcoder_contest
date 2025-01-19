N = int(input())
A = list(map(int,input().split()))

koma = [0,0,0,0]
ans = 0
for x in A:
    next_koma = [0,0,0,0]
    koma[0] = 1
    for i in range(4):
        if koma[i] == 1:
            if i+x >= 4:
                ans += 1
            else:
                next_koma[i+x] = 1
    koma = next_koma

print(ans)
    
