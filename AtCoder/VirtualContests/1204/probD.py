# Mまでの素数全列挙(エラトステネスの篩)
def primes(M):
    is_prime = [-1 for _ in range(M+1)]
    for m in range(2, M+1):
        if is_prime[m] == -1:
            is_prime[m] = 1
            l = 2
            while m*l <= M:
                is_prime[m*l] = 0
                l += 1
    primes = []
    for p in range(2, M+1):
        if is_prime[p] == 1:
            primes.append(p)
    return primes

N = int(input())

P = primes(55555)
A = []
for p in P:
    if p%5 == 2:
        A.append(p)
    if len(A) == N: break
print(' '.join([str(a) for a in A]))