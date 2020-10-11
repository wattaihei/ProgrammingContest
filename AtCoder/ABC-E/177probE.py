
import sys
input = sys.stdin.buffer.readline
from math import gcd

N = int(input())
A = list(map(int, input().split()))

# Mまでの素数全列挙(エラトステネスの篩)
def primes(M):
    B = set(A)
    if (1 in B and len(A) != len(B) + A.count(1)-1) or (not 1 in B and len(A) != len(B)):
        return False
    ok = True
    is_prime = [-1 for _ in range(M+1)]
    for m in range(2, M+1):
        if is_prime[m] == -1:
            is_prime[m] = 1
            cnt = 0
            if m in B: cnt += 1
            l = 2
            while m*l <= M:
                if m*l in B:
                    cnt += 1
                is_prime[m*l] = 0
                l += 1
            if cnt > 1:
                ok = False
                break
    return ok

def check():
    k = A[0]
    for a in A:
        k = gcd(a, k)
    return k == 1

if primes(10**6):
    ans = "pairwise coprime"
elif check():
    ans = "setwise coprime"
else:
    ans = "not coprime"
print(ans)