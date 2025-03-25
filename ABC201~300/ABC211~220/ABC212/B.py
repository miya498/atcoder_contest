X = input()

same,step = True,True

for i in range(3):
    if X[i] != X[i+1]:
        same = False
    if (int(X[i])+1)%10 != int(X[i+1]):
        step = False

if (same or step):
    print("Weak")
else:
    print("Strong")