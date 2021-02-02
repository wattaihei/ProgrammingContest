# (x0, y0) of ax + by = 1
def oneOfSolution(a, b):
    if b == 1:
        return 0, 1
    d = a//b
    p, q = oneOfSolution(b, a%b)
    return q, p-d*q


def euler_phi(n):
    primes = []
    tmp = n
    for a in range(2, int(sqrt(n))+3):
        if tmp%a == 0:
            primes.append(a)
            while tmp%a == 0:
                tmp //= a
    if tmp > 1: primes.append(tmp)
    ret = n
    for p in primes:
        ret = ret * (p-1) // p
    return ret