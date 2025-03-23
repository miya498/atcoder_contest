X = input()
pos = X.find(".")
if pos != -1:
    X = X[:pos]

print(X)