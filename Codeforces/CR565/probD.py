
from bisect import bisect_left, bisect_right
from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
B = list(map(int, input().split()))



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
    return primes, is_prime


primes, is_prime = primes(2750140)

B.sort(reverse=True)
C = Counter(B)

A = []
for b in B:
    if C[b] == 0:
        continue
    if is_prime[b]:
        a = bisect_right(primes, b)
        C[a] -= 1
        C[b] -= 1
        A.append(a)
    else:
        for p in primes:
            if b % p == 0:
                a = b//p
                break
        C[a] -= 1
        C[b] -= 1
        A.append(b)

for a in A:
    print(a, end=' ')
print()
