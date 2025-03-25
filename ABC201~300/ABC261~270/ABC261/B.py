N = int(input())
A = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if A[i][j] == "-":
            continue
        elif A[i][j] == "L":
            if A[j][i] != "W":
                print("incorrect")
                exit()
        elif A[i][j] == "W":
            if A[j][i] != "L":
                print("incorrect")
                exit()
        elif A[i][j] == "D":
            if A[j][i] != "D":
                print("incorrect")
                exit()
print("correct")