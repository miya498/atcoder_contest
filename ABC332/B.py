K,G,M = map(int,input().split())

glass = 0
magcup = 0
for _ in range(K):
    if glass == G:
        glass = 0
    elif magcup == 0:
        magcup = M
    else:
        utusu = min(magcup,G-glass)
        magcup = magcup - utusu
        glass = glass + utusu
    

print(glass,magcup)