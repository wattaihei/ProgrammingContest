import math
from bisect import bisect_left, bisect_right

Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]

is_prime = [False for _ in range(100001)]
is_prime[3] = True
primes = [3]
for n in range(5, 100001, 2):
    prime = True
    i = 2
    while i < int(math.sqrt(n)) + 1:
        if n % i == 0:
            prime = False
            break
        i += 1
    if prime:
        primes.append(n)
        is_prime[n] = True

like = []
for p in primes:
    if p == 3:
        like.append(p)
        continue
    q = (p+1)//2
    if is_prime[q]:
        like.append(p)

for l, r in LR:
    ans = bisect_right(like, r) - bisect_left(like, l)
    print(ans)