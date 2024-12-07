def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(limit + 1) if is_prime[i]]

N = int(input())
primes = sieve_of_eratosthenes(int(N**0.5) + 1)
ans = 0

for p in primes:
    if p**8 > N:
        break
    ans += 1

for i in range(len(primes)):
    if primes[i]**4 > N:
        break
    for j in range(i + 1, len(primes)):
        if primes[i]**2 * primes[j]**2 > N:
            break
        ans += 1

print(ans)