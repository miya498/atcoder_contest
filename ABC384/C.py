from itertools import combinations
a,b,c,d,e = map(int,input().split())

score = {"A":a, "B":b, "C":c,"D":d,"E":e}

ans = []

for i in range(1,6):
    for con in combinations("ABCDE",i):
        name = "".join(con)
        s = sum(score[p] for p in con)
        ans.append((s,name))

ans.sort(key=lambda x: (-x[0],x[1]))

for s,n in ans:
    print(n)