def g1(num):
    return int("".join(sorted(str(num),reverse=True)))
def g2(num):
    return int("".join(sorted(str(num))))

N,K = map(int,input().split())
for _ in range(K):
    N = g1(N)-g2(N)
print(N)