import sys
input = sys.stdin.buffer.readline

MAX = 10**10

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
        if is_prime[p] == 1 and p**3 <= MAX:
            primes.append(p)
    return primes


if __name__ == "__main__":
        
    N = int(input())
    A = [int(input()) for _ in range(N)]

    P = primes(10**5)

    ans = 0
    elements = {}
    invs = {}
    for a in A:
        fac = 1
        inv = 1
        for p in P:
            if p > a: break
            c = 0
            while a%p == 0:
                a //= p
                c += 1
            c %= 3
            fac *= p**c
            inv *= p**((3-c)%3)
        elements[(fac, a)] = elements.get((fac, a), 0) + 1
        invs[fac] = inv

    score = 0
    is_inv = set()
    for (a, r), c in elements.items():
        if r == 1:
            if a == 1:
                ans += 1
            else:
                b = invs[a]
                if (b, 1) in elements:
                    score += max(elements[(b, 1)], c)
                else:
                    ans += c
        else:
            if (invs[a], r**2) in elements:
                is_inv.add((invs[a], r**2))
    
    for (a, r), c in elements.items():
        if r > 1:
            if (a, r) in is_inv: continue
            ans += max(elements.get((invs[a], r**2), 0), c)

    ans += score//2
    print(ans)