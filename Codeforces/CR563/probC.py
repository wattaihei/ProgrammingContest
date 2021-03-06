N = int(input())

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

P = primes(N)
ans = [None]*(N+1)

for i, p in enumerate(P):
    k = p
    while k <= N:
        if ans[k] is None:
            ans[k] = i+1
        k += p

for n in range(2, N+1):
    print(ans[n], end=' ')
print()