from collections import Counter


S = input()

flag = True

if len(S)%2 == 0:
    for i in range(len(S)//2-1):
        
        if S[2*i] != S[2*i+1]:
            flag = False
        
    cnt = Counter(S)
    if not all(count == 2 for count in cnt.values()):
        flag = False
        
else:
    flag = False

if flag:
    print("Yes")
else:
    print("No")