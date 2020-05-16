import math
N = 600851475143

def prime(n):
    factor = []
    tmp = int(math.sqrt(n)) + 1
    for num in range(2, tmp):
        while n % num == 0:
            n //= num
            factor.append(num)
    if n != 1:
        factor.append(n)
    return factor

print(max(prime(N)))