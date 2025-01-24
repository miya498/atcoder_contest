V,A,B,C = map(int,input().split())

t = 0
while True:
    if t%3 == 0:
        if V < A:
            print("F")
            exit()
        else:
            V -= A
            t += 1
    elif t%3 == 1:
        if V < B:
            print("M")
            exit()
        else:
            V -= B
            t += 1
    else:
        if V < C:
            print("T")
            exit()
        else:
            V -= C
            t += 1