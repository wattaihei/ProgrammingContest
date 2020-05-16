import math

N, K = map(int, input().split())
A = list(map(int, input().split()))

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

primes = primes(10**5)
dic = {}
for p in primes:
    dic[p] = [[] for _ in range(K)]

for a in A:
    b = a
    tmp = int(math.sqrt(a)) + 1
    for num in range(2, tmp):
        c = 0
        while a % num == 0:
            a //= num
            c += 1
        dic[num][c%K].append(b)
    if a != 1:
        dic[a][1].append(b)

print(dic)