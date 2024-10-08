N = int(input())
S = list(input())
Q = int(input())

alpa = 'abcdefghijklmnopqrstuvwxyz'

for __ in range(Q):
    c,d = map(str,input().split())
    alpa = alpa.replace(c,d)


for i in range(N):
    #アスキーコード取得
    num = ord(S[i])-97
    S[i] = alpa[num]

print(''.join(S))
