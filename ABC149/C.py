X = int(input())

while True:
    i = 2
    while i <= X**0.5:
        if X % i == 0:
            break
        i += 1
    if i > X**0.5:
        print(X)
        break
    else:
        X += 1
