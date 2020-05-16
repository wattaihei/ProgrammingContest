N = int(input())

primes = []
for n in range(2, 55556):
    i = 2
    prime = True
    while i**2 <= n:
        if n % i == 0:
            prime = False
            break
        i += 1
    if prime and n % 5 == 1:
        primes.append(n)

for i in range(N):
    print(primes[i], end=' ')
print()