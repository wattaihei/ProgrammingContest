primes = [2]
n = 2
while len(primes) < 10001:
    n += 1
    is_prime = True
    for p in primes:
        if n % p == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(n)
print(primes[-1])