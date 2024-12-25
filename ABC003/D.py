R,C = map(int,input().split())
X,Y = map(int,input().split())
D,L = map(int,input().split())

def factorial_naive(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result