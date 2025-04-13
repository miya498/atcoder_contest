N,M = map(int,input().split())
S = list(input())

mugi = M
mugi_siyou = 0
logo = 0
logo_siyou = 0
for i in range(N):
    if S[i] == "0":
        mugi += mugi_siyou
        logo += logo_siyou
        mugi_siyou = 0
        logo_siyou = 0
    elif S[i] == "1":
        if mugi == 0:
            if logo == 0:
                logo_siyou += 1
            else:
                logo -= 1
                logo_siyou += 1
        else:
            mugi -= 1
            mugi_siyou += 1
    else:
        if logo == 0:
            logo_siyou += 1
        else:
            logo -= 1
            logo_siyou += 1

print(logo+logo_siyou)